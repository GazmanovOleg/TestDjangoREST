from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'filename', )




class FileIdRequestSerializer(serializers.Serializer):
    id = id,
    filename = serializers.CharField(),
    processing = serializers.BooleanField(),
    processingSuccess = serializers.BooleanField()