from rest_framework import serializers
from .models import File

# class HelloSerializer(serializers.Serializer):
#     """Serializes a name field for testing out APIView"""
#     obj = serializers.CharField(max_length=10)

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
        #fields = ('name', )
