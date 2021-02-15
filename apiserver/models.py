from django.db import models

# Create your models here.
class Imgdata(models.Model):
    imgname=models.CharField(null=True, max_length=50)
    bigcategory=models.CharField(null=True, max_length=50)
    middlecategory=models.CharField(null=True, max_length=50)
    furniturename=models.CharField(null=True, max_length=50)
    style=models.CharField(null=True, max_length=50)
    selectfd=models.CharField(null=True, max_length=50)
    price=models.IntegerField(null=True, blank=False)
    color=models.IntegerField(null=True, blank=False)
    detail=models.CharField(null=True, max_length=50)
    image=models.ImageField(blank=True, upload_to="", null=True)

class Upload(models.Model):
    image=models.FileField(blank=False, null=False)