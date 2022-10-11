from django.urls import path, include
from . import views

app_name = 'video'
urlpatterns = [
    path('add-video/', views.add_video, name = "add_video"),
    path('video-details/<int:id>/', views.video_details, name = "video_details"),
]