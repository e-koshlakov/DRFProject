from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.validators import PasswordValidator
from users.models import User


class UserSerializer(TokenObtainPairSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'is_active',)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=16, )

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone', 'is_active',)
        validators = [PasswordValidator(field='password')]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'is_active',)
        validators = [PasswordValidator(field='password')]


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
