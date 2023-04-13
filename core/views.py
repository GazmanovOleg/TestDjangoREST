from django.forms import model_to_dict
from rest_framework import generics
import uuid
import json
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import File
from .serializers import FileSerializer, FileIdRequestSerializer, FileRequestSerializer
class FileAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileIdRequestView(APIView):
    def patch(self, request, id = None):
        file = File.objects.filter(id = id)
        file_dict = file.values()[0]

        width =  request.data.get('width')
        height = request.data.get('height')
        file.width = width
        file.heigth = height 
        
        input_file = file_dict['video']
        output_file = "result.mp4"

        os.system(f"ffmpeg -i {input_file} -s {width}x{height} {output_file}")

        file.video = output_file
        return Response({'width':width, 'height':height})
    
    def delete(self, request, id = None):
        file = File.objects.filter(id = id)
        file.delete()
        "Написать проверку"
        file_list = File.objects.all().values()
        print(file_list)
        return Response({'success':True})

    def get(self, request, id = None):
        file = File.objects.filter(id = id)
        print(file)
        return Response(FileIdRequestSerializer(file, many=True).data)



class FileRequestView(APIView):
    def post(self, request):
        file = File.objects.create(
            video = request.data.get("video")
        )
        print(file.video)
        file.save()
        print(file.video)

        return Response({'id': file.id})