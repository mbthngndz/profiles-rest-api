from abc import ABC

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from profiles_api import models
from profiles_api.models import ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {  # Password field'ını user profile
            "password": {  # list bölümünde göstermemek için
                'write_only': True,  # write_only kullanılır.
                'style': {'input_type': 'password'}  # Parolanın gözükmemesini sağlar.
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
   """Serializers profile feed items"""

   class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


            ####### Api View serializer ##########

class FeedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeedItem
        fields = '__all__'


class FeedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeedItem
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}

        def create(self, validated_data):
            user_profile = validated_data.get('user_profile')
            status_text = validated_data.get('status_text')
            created_on = validated_data.get('created_on')

            user_obj = ProfileFeedItem(
                user_profile=user_profile,
                status_text=status_text,
                created_on=created_on
            )
            user_obj.save()
            data = user_obj
            return data


