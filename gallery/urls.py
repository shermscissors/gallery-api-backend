from django.urls import path
from . import views

urlpatterns = [
    path('photos/', views.Photo.as_view(), name='photos_list'),
    path('photos/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'),
]
