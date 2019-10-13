from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=40)
    price = models.FloatField()
    qty = models.IntegerField()
    remarks = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    vendor= models.CharField(max_length=40)
    brand = models.CharField(max_length=40)

    class Meta:
        db_table="Product_Info"

