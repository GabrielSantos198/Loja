from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class HomePageSlideShow(TimeStampedModel):
    slide_0_title = models.CharField(max_length=40, blank=False)
    slide_1_title = models.CharField(max_length=40, blank=False)
    slide_2_title = models.CharField(max_length=40, blank=False)

    slide_0_text = models.CharField(max_length=100, blank=False)
    slide_1_text = models.CharField(max_length=100, blank=False)
    slide_2_text = models.CharField(max_length=100, blank=False)

    
class InstagramSection(TimeStampedModel):
    instagram_0_image = models.ImageField(upload_to='instagram/%Y/%m/%d', blank=True, default='no_image')
    instagram_1_image = models.ImageField(upload_to='instagram/%Y/%m/%d', blank=True, default='no_image')
    instagram_2_image = models.ImageField(upload_to='instagram/%Y/%m/%d', blank=True, default='no_image')
    instagram_3_image = models.ImageField(upload_to='instagram/%Y/%m/%d', blank=True, default='no_image')
    instagram_4_image = models.ImageField(upload_to='instagram/%Y/%m/%d', blank=True, default='no_image')

    instagram_0_text = models.TextField()
    instagram_1_text = models.TextField()
    instagram_2_text = models.TextField()
    instagram_3_text = models.TextField()
    instagram_4_text = models.TextField()


class AboutPage(TimeStampedModel):
    about = models.TextField()
    image = models.ImageField(upload_to='about/%Y/%m/%d', blank=True, default='no_image')
