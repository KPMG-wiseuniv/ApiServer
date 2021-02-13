from django.db import models

# Create your models here.
class Imgdata(models.Model):
    imgname=models.CharField(max_length=50)
    bigcategory=models.CharField(max_length=50)
    middlecategory=models.CharField(max_length=50)
    furniturename=models.CharField(max_length=50)
    image=models.ImageField(blank=True, upload_to="", null=True)