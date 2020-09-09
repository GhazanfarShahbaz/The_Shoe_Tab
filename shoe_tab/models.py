from django.db import models

class Shoe(models.Model):
    """The Shoe class for acessing and putting in new shoe data"""
    shoe_brand = models.CharField(max_length=16)    # hoe brand for filtering
    shoe_name = models.CharField(max_length=128)    # name of the shoe
    release_date = models.CharField(max_length=16)  # release date
    release_time = models.CharField(max_length=16)  # release time
    image = models.URLField()                       # image url
    price = models.CharField(max_length=16)         # drop price
    hyped= models.BooleanField()                    # if shoe is hyped or not
