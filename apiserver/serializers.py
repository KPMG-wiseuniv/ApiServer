from rest_framework import serializers
from .models import Imgdata

class ImgdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Imgdata
        fields='__all__'