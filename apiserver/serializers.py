from rest_framework import serializers
from .models import Imgdata, Upload

class ImgdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Imgdata
        fields='__all__'

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upload
        fields='__all__'