from django.db import models

# Create your models here.


class ActiveVendors(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='YES')


class InActiveVendors(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='NO')




class Vendor(models.Model):
    name=models.CharField(max_length=40)
    active = models.CharField(max_length=40,default='YES')
    allven = models.Manager()
    actven = ActiveVendors()
    iactven = InActiveVendors()

    class Meta:
        db_table="Vendor_Info"


if __name__ == '__main__':
        v1 = Vendor(id=101,name='Flipkart',active='YES')
        v2 = Vendor(id=102,name='Snapdeal',active='YES')
        v3 = Vendor(id=103,name='Amazon',active='YES')
        v1.save()
        v2.save()
        v3.save()