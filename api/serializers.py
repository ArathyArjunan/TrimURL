from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Link

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'original_url', 'short_code', 'clicks', 'created_at']
        read_only_fields = ['short_code', 'clicks', 'created_at']
