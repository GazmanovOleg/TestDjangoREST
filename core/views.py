from django.forms import model_to_dict
from rest_framework import generics
import uuid
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import File
from .serializers import FileSerializer, FileIdRequestSerializer
class FileAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileIdRequest(APIView):
    def patch(self, request, id = None):
        pass
    
    def delete(self, request, id = None):
        pass

    def get(self, request, id = None):
        file = File.objects.filter(id = id)
        return Response({"data": FileIdRequestSerializer(file, many=True).data})



