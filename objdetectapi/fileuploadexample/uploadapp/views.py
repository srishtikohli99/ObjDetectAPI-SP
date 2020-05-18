from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from uploadapp import serializers
from .serializers import FileSerializer
from .face_recognition import *
#from .models import objectDetect



class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
        
        file_serializer = FileSerializer(data=request.data)
        #serializer_class = serializers.HelloSerializer
        # serializer =HelloSerializer(data=request.data)
        # if serializer.is_valid():
        #     obj = serializer.validated_data.get('obj')
            
        #mod1 = objectDetect
        if file_serializer.is_valid():
            print(type(file_serializer))
            file_serializer.save()
            i = objectDetect()
            return Response(i, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

