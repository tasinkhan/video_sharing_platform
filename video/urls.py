from django.urls import path, include
from . import views

app_name = 'video'
urlpatterns = [
    path('add-video/', views.add_video, name = "add_video"),
    path('video-details/<int:id>/', views.video_details, name = "video_details"),
    path('like-video/<str:id>/', views.like_video, name = "like_video"),
    path('dislike-video/<str:id>/', views.dislike_video, name = "dislike_video"),
]