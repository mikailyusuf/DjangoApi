from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
        # validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True
        # validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(max_length=8)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'last_name',
            'first_name'
        )

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']