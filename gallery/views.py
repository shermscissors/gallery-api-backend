from rest_framework import generics
from .models import Photo
from .serializers import PhotoSerializer

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Photo.objects.all()
   serializer_class = PhotoSerializer
   
class Photo(generics.ListCreateAPIView):
   queryset = Photo.objects.all()
   serializer_class = PhotoSerializer
