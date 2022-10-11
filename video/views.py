from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Video, Like, Dislike
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

def like_video(request, id):
    if request.method == "POST":
        
        video_obj = Video.objects.get(id = id)

        print(video_obj)
        # print(video_obj.title)
        # print(video_obj.like.user.all())
        if request.user in video_obj.like.user.all():
            print("--------------------------------")
            video_obj.like.user.remove(request.user)
            video_obj.save()
            return HttpResponse("like removed")
        else:
            print("=====================")
            try:
                liked_obj = Like.objects.get(video = video_obj.id)
            except:
                liked_obj = None
            if liked_obj is not None:
                liked_obj.user.add(request.user)                
                return HttpResponse("liked")
            else:
                like_obj = Like.objects.create(video = video_obj)
                like_obj.user.add(request.user)
                return HttpResponse("liked")
        # print(id)
        # print(request.user)
        # print(request.POST)
        
        

    