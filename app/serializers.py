from django.contrib.auth.models import User, Permission
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.id = validate_data.get('id')
        instance.username = validate_data.get('username')
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def update(self, instance, validate_data):
        instance.username = validate_data.get('username')
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save(force_update = True)
        return instance

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
