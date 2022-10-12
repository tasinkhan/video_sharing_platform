from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Video, Like, Dislike
from users.models import User
import sweetify
import json

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
        liked = None
        video_obj = Video.objects.get(id = id)
        try:
            liked_obj = Like.objects.get(video = video_obj.id)
        except:
            liked_obj = None

        try:
            disliked_obj = Dislike.objects.get(video = video_obj.id)
        except:
            disliked_obj = None

        if liked_obj:
            if request.user in video_obj.like.user.all():
                print("--------------------------------")
                video_obj.like.user.remove(request.user)
                video_obj.save()
                return HttpResponse(json.dumps({'liked':False, 'video_id':id}))
            
            else:
                liked_obj.user.add(request.user)
                if disliked_obj:
                    disliked_obj.user.remove(request.user)
                return HttpResponse(json.dumps({'liked':True, 'video_id':id}))
        else:
            print("=====================")
            
            like_obj = Like.objects.create(video = video_obj)
            like_obj.user.add(request.user)
            if disliked_obj:
                disliked_obj.user.remove(request.user)
            return HttpResponse(json.dumps({'liked':True, 'video_id':id}))


def dislike_video(request, id):
    if request.method == "POST":
        video_obj = Video.objects.get(id = id)
        try:
            disliked_obj = Dislike.objects.get(video = video_obj.id)
        except:
            disliked_obj = None

        try:
            liked_obj = Like.objects.get(video = video_obj.id)
        except:
            liked_obj = None

        if disliked_obj:
            if request.user in video_obj.dislike.user.all():
                print("--------------------------------")
                video_obj.dislike.user.remove(request.user)
                video_obj.save()
                return HttpResponse("dislike removed")
            
            else:
                disliked_obj.user.add(request.user)
                if liked_obj:
                    liked_obj.user.remove(request.user)
                return HttpResponse("disliked")
        else:
            print("=====================")
            
            dislike_obj = Dislike.objects.create(video = video_obj)
            dislike_obj.user.add(request.user)
            if liked_obj:
                liked_obj.user.remove(request.user)
            return HttpResponse("disliked")
        
        

    