from rest_framework import serializers
from .models import User
from django.utils import timezone
from datetime import date , timedelta
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
             
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data['user_type'] = 'user'
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)  # Hash the password
            user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)


from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [ 'video_file' , 'uploaded_at']
