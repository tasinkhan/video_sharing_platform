from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Video, Like, Dislike
from users.models import User
import sweetify
import json
from django.contrib.auth.decorators import login_required

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

@login_required
def like_video(request, id):
    if request.method == "POST":
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
                video_obj.like.user.remove(request.user)
                video_obj.save()
                like_count = video_obj.like.user.count()
                context = {'liked':False, 'video_id':f"{id}_like", "like_count":like_count}
                return HttpResponse(json.dumps(context))
            
            else:
                liked_obj.user.add(request.user)
                like_count = video_obj.like.user.count()
                if disliked_obj:
                    disliked_obj.user.remove(request.user)
                context = {'liked':True, 'video_id':f"{id}_like", "like_count":like_count}
                
                return HttpResponse(json.dumps(context))
        else:
            like_obj = Like.objects.create(video = video_obj)
            like_obj.user.add(request.user)
            like_count = video_obj.like.user.count()
            if disliked_obj:
                disliked_obj.user.remove(request.user)
            context = {'liked':True, 'video_id':f"{id}_like", "like_count":like_count}
            return HttpResponse(json.dumps(context))

@login_required
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
                dislike_count = video_obj.dislike.user.count()
                context = {'disliked':False, 'video_id':f"{id}_dislike", "dislike_count":dislike_count}
                return HttpResponse(json.dumps(context))
            
            else:
                disliked_obj.user.add(request.user)
                if liked_obj:
                    liked_obj.user.remove(request.user)
                dislike_count = video_obj.dislike.user.count()
                context = {'disliked':True, 'video_id':f"{id}_dislike", "dislike_count":dislike_count}
                return HttpResponse(json.dumps(context))
        else:
            print("=====================")
            
            dislike_obj = Dislike.objects.create(video = video_obj)
            dislike_obj.user.add(request.user)
            if liked_obj:
                liked_obj.user.remove(request.user)
            dislike_count = video_obj.dislike.user.count()
            context = {'disliked':True, 'video_id':f"{id}_dislike", "dislike_count":dislike_count}
            return HttpResponse(json.dumps(context))
        
        

    