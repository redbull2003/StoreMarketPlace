# Standard library import
from django.db.models import Q

# Third-party import
from django.core.exceptions import ValidationError
from rest_framework import serializers

# Local import
from Account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'username',
            'email',
            'phone_number',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}


class CreateNewUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
         )
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        username = data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('نام کاربری وارد شده قبلا ثبت شده است')
        return data
    
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        user_obj = User(
            username=username
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=70)
    token = serializers.CharField(max_length=300, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'token', 'password')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password')
        if not username:
            raise ValidationError('نام کاربری خود را وارد کنید')
                    
        user = User.objects.filter(
            Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('نام کاربری یافت نشد')
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('رمز عبور اشتباه است')
            data['token'] = 'some random token'
        return data


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
        Serializer for password change endpoint
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)