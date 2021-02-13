from django.shortcuts import render
from .models import Imgdata
from .serializers import ImgdataSerializer
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