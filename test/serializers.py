from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from test import models
from test.models import Test, TestFeedItem
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers


class TestModelSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = [
            'id',
            "description",
            "sub_name",
            "link",
            "country",
            "language",
        ]
        extra_kwargs = {"sub_name": {"required": False}, "link": {"required": False}}


class TestFeedItemSerializer(serializers.ModelSerializer):
    """Serializers profile feed items"""

    class Meta:
        model = TestFeedItem
        fields = ('id', 'feed_text')
