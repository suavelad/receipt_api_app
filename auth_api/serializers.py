from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User


class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, args, *kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    """
    Serializer for SID Staffs  ( Q.A, Q.C,etc) Registration.
    """
    class Meta:
        model = User
        read_only_fields = ('id', 'is_admin', 'time_created', 'last_login', 'date_created')
        exclude = ('groups', 'is_superuser', 'is_staff', 'is_admin', 'user_permissions', 'date_joined', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        group = Group.objects.get(name='adm')
        user.groups.add(group)
        return user


class CashierSerializer(serializers.ModelSerializer):
    """
    Serializer for SID Staffs  ( Q.A, Q.C,etc) Registration.
    """
    class Meta:
        model = User
        read_only_fields = ('id', 'is_admin', 'time_created', 'last_login', 'date_created')
        exclude = ('groups', 'is_superuser', 'is_staff', 'is_admin', 'user_permissions', 'date_joined', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        group = Group.objects.get(name='csh')
        user.groups.add(group)
        return user

