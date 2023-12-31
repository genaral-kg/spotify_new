from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name', 'age', 'password', 'password2')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError('Passwords did not match!')
        if attrs['password'].isalpha():
            raise serializers.ValidationError('Password field must contain' 'alpha symbols and numbers')
        if attrs['password'].isdigit():
            raise serializers.ValidationError('Password field must contain' 'alpha symbols and numbers')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {'Bad token': _('Token is invalid or expired!')}

    def validate(self,attrs):
        self.token  = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')

# TODO: Suggestions for Improvement Handling Token Errors: The except TokenError block is correctly used to handle
#  invalid or expired tokens. Ensure that the error message returned to the user is informative yet secure.
#  Serializer Usage: Ensure that your corresponding view correctly uses this serializer to perform the logout operation.
