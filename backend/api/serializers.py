from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, UserRole, MenuItem, RoleMenuAccess

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class RoleMenuAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleMenuAccess
        fields = '__all__'