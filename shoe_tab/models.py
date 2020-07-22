from django.db import models

# Create your models here.


class shoe_data(models.Model):
    shoe_name = models.CharField(max_length = 200)
    shoe_price = models.CharField(max_length = 6)
    shoe_release_date = models.DateTimeField()

