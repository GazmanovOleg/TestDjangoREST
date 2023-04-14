from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'filename','video' )




class FileIdRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id','filename','processing','processingSuccess','video' )

class FileVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('video',)

class FileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id',)