from django.db import models

# Create your models here.


# class shoe_data(models.Model):
#     shoe_name = models.CharField(max_length = 200)
#     shoe_price = models.CharField(max_length = 6)
#     shoe_release_date = models.DateTimeField()

#     def __str__(self):
#         return f"Name: {shoe_name} \nPrice: {shoe_price} \n{shoe_release_date}"


class Shoe(models.Model):
    """The Shoe class for acessing and putting in new shoe data"""
    shoe_brand = models.CharField(max_length=16)
    shoe_name = models.CharField(max_length=128)
    release_date = models.CharField(max_length=16)
    release_time = models.CharField(max_length=16)
    image = models.URLField()
    price = models.CharField(max_length=16)
    hyped= models.BooleanField()