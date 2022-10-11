from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Video
from users.models import User
import sweetify

# Create your views here.

def add_video(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        url = request.POST['url']
        try:
            qs = Video.objects.get(title = title)
        except:
            qs = None
        if qs is not None:
            sweetify.error(request,"Video title already exists")
            return redirect('users:dashboard')
        else:
            video = Video.objects.create(title = title, url = url, added_by = user)
            sweetify.success(request,"Video added successfully")
            return redirect('users:dashboard')

def video_details(request, id):
    if request.method == "POST":
        video = Video.objects.get(id = id)
        print(video.added_by.email)
    return HttpResponse(request, )
    