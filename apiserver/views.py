from django.shortcuts import render
from .models import Imgdata, Upload
from .serializers import ImgdataSerializer, UploadSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
def send_imgdata(request):
    if request.method=='GET':
        query_set=Imgdata.objects.all()
        serializer=ImgdataSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def train_img(request):
    if request.method=='POST':
        img_serializer=UploadSerializer(data=request.FILES)
        if img_serializer.is_valid():
            img_serializer.save()
        return HttpResponse()