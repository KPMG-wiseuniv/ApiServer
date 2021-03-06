from django.shortcuts import render
from .models import Imgdata, Upload
from .serializers import ImgdataSerializer, UploadSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import torch, torchvision
from PIL import Image
import os
import numpy as np
from .FR_model import *
import json
from collections import OrderedDict
#import cv2
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
        global imgname
        global Furniture
        global FD
        imgname=request.POST['imgname']
        imgname=imgname.replace('"', '')
        imgname='media/'+imgname
        Furniture=request.POST['Furniture']
        FD=request.POST['FD']
        Furniture=Furniture.replace('"', '')
        FD=FD.replace('"', '')
        print(imgname)
        print(Furniture)
        print(FD)
        if img_serializer.is_valid():
            img_serializer.save()
        return HttpResponse()

@csrf_exempt
def send_train_result(request):
    img=os.path.join(os.path.dirname(os.path.dirname(__file__)),imgname)
    #img=os.path.join(os.path.dirname(os.path.dirname(__file__)),'media/sam.PNG')
    #img=cv2.imread(img)
    img=Image.open(img)
    print(np.array(img).shape)
    img=img.convert('RGB')
    print(np.array(img).shape)
    img=np.expand_dims(np.transpose(img, (2, 0, 1)), 0)
    img_t=torch.as_tensor(img, dtype=torch.float)
    global model
    if img is None:
        print('Image load failed')
        return HttpResponse()
    else:
        print(Furniture)
        print(FD)
        if Furniture=='Chair':
            model=mobilenet_v3_small(num_classes=[2, 6, 3, 4])
            model.load_state_dict(torch.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),'media/200_chair.pth')))
        elif Furniture=='Table':
            model=mobilenet_v3_small(num_classes=[2, 6, 3, 3])
            model.load_state_dict(torch.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),'media/200_table.pth')))
        if model is None:
            print('model load failed')
            return HttpResponse()
        else:
            model.eval()
            output=model(img_t)
            interior=np.argmax(output[0].detach().numpy(), axis = 1)
            color=output[1].detach().numpy()
            if int(interior[0])==0:
                color[0][3]=0
                color[0][4]=0
                color[0][5]=0
            elif int(interior[0])==1:
                color[0][0]=0
                color[0][2]=0
            color=np.argmax(color, axis = 1)
            output_design=output[2].detach().numpy()
            output_function=output[3].detach().numpy()
            output_design[0][0]=0
            output_function[0][0] =0
            FR_design=np.argmax(output_design, axis=1)
            FR_function=np.argmax(output_function, axis = 1)
            interior=interior[0]
            color=color[0]
            FR_design=FR_design[0]
            FR_function=FR_function[0]
            print(interior)
            print(color)
            print(FR_design)
            print(FR_function)
            if FD=='Design':
                result=OrderedDict()
                result["interior"]=int(interior)
                result["color"]=int(color)
                result["FD"]=int(FR_design)
                return JsonResponse(result)
            elif FD=='Function':
                result=OrderedDict()
                result["interior"]=int(interior)
                result["color"]=int(color)
                result["FD"]=int(FR_function)
                return JsonResponse(result)
    return HttpResponse()

