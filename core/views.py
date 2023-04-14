from django.forms import model_to_dict
from rest_framework import generics
from .logs import logger
from .tasks import change_video_extension
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import File
from .serializers import FileSerializer, FileIdRequestSerializer, FileRequestSerializer, FileVideoSerializer
import string
import random
import os
def get_random_string(string_len = 6):
    return ''.join(string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase))] for _ in range(string_len))


class FileAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileIdRequestView(APIView):
    def patch(self, request, id = None):
        file = File.objects.get(id = id)
        #file_dict = file.values()[0]

        width =  request.data.get('width')
        height = request.data.get('height')
        file.width = width
        file.height = height 
        
        #print(type(change_video_extension.delay(input_file, width, height)))
        #print(f'!!!!!!!!!!!!!{FileVideoSerializer(change_video_extension.delay(input_file, width, height), many = True).data}!!!!!')
        #print(f"output_file type --{type(n)} output_file_name ---{n}")
        #file.video = n
        #print(file.video)
        
        #input_file = file.video
        #output_file = f"{get_random_string()}.mp4"
        #os.system(f"ffmpeg -i {input_file} -s {width}x{height} {output_file}")
        #file.video = output_file
       
        file.video=change_video_extension.delay(file.video.path, width, height)
        print(f"!!!!!!!!!!!!!!!!{file.video}!!!!!!!!!")
        #file.video = new_video.video
        file.save()
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