from django.db import models
#from django_resized import ResizedImageField
#from PIL import Image
from profiles_project import settings


class Test (models.Model):

    country = models.CharField(max_length=300, blank=True, null=True, unique=False, default='Common')
    language = models.CharField(max_length=300, blank=True, null=True, unique=False, default='English')
    description = models.CharField(max_length=3000, blank=False, null=False, unique=False, default='a')
    sub_name = models.CharField(max_length=300, blank=True, null=True, unique=False, default='')
    link = models.CharField(max_length=300, blank=True, null=True, unique=False, default='')




class TestFeedItem(models.Model):
    """Profile status update"""

    feed_text = models.CharField(max_length=255)



