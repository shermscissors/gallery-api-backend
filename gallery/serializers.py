from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    photo_detail = serializers.ModelSerializer.serializer_url_field(
        view_name='photo_detail')

    class Meta:
        model = Photo
        fields = ('title', 'photo_url', 'photo_detail')
