from django.db import models


class Shoe(models.Model):
    """The Shoe class for acessing and putting in new shoe data"""
    shoe_brand = models.CharField(max_length=16)                # shoe brand for filtering
    shoe_name = models.CharField(max_length=128, unique=True)   # name of the shoe
    release_day = models.IntegerField()                         # release day field
    release_month = models.IntegerField()                       # release month field
    release_year = models.IntegerField()                        # release year field
    release_time = models.CharField(max_length=16)              # release time
    image = models.URLField()                                   # image url
    price = models.CharField(max_length=16)                     # drop price
    hyped = models.BooleanField()                               # if shoe is hyped or not
