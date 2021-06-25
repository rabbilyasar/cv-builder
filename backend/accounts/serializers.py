from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProfileUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',
                  'username',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'phone',
                  'address',
                  'postcode',
                  'city',
                  'country',
                  'country_code',
                  'website',
                  'marital_status',
                  'date_of_birth',
                  'nacionality',
                  'military_service',
                  'driving_license',
                  'job_title',
                  'created_at',
                  'updated_at')


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
