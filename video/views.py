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
            video = Video.objects.create(title = title, embded_video = url, added_by = user)
            sweetify.success(request,"Video added successfully")
            return redirect('users:dashboard')

def video_details(request, id):
    if request.method == "POST":
        video = Video.objects.get(id = id)
        print(video.added_by.email)
    return HttpResponse(request, )

# @login_required(login_url='/users/login/')
def like_video(request, id):    
    if request.method == "POST":
        print(request.POST)
        is_logged_in = False
        if request.user.is_authenticated:
            is_logged_in = True
            video_obj = Video.objects.get(id = id)
            try:
                liked_obj = Like.objects.get(video = video_obj.id)
            except:
                liked_obj = None

            try:
                disliked_obj = Dislike.objects.get(video = video_obj.id)
            except:
                disliked_obj = None
            liked = False

            if disliked_obj:
                dislike_count = video_obj.dislike.user.count()
            else:
                dislike_count = 0

            disliked_video_id = f"{id}_dislike"
            if liked_obj:
                if request.user in video_obj.like.user.all():
                    video_obj.like.user.remove(request.user)
                    video_obj.save()
                    like_count = video_obj.like.user.count()
                    liked = False
                    context = {'liked':liked, 'video_id':f"{id}_like", "like_count":like_count, 'disliked_video_id':disliked_video_id, 'dislike_count':dislike_count, "is_logged_in":is_logged_in}
                    return HttpResponse(json.dumps(context))
                
                else:
                    liked_obj.user.add(request.user)
                    like_count = video_obj.like.user.count()
                    if disliked_obj:
                        disliked_obj.user.remove(request.user)
                        dislike_count = video_obj.dislike.user.count()
                    else:
                        dislike_count = dislike_count
                    liked = True
                    context = {'liked':liked, 'video_id':f"{id}_like", "like_count":like_count, 'disliked_video_id':disliked_video_id, 'dislike_count':dislike_count, "is_logged_in":is_logged_in}
                    
                    return HttpResponse(json.dumps(context))
            else:
                like_obj = Like.objects.create(video = video_obj)
                like_obj.user.add(request.user)
                like_count = video_obj.like.user.count()
                if disliked_obj:
                    disliked_obj.user.remove(request.user)
                    dislike_count = video_obj.dislike.user.count()
                else:
                    dislike_count = dislike_count

                liked = True
                context = {'liked':liked, 'video_id':f"{id}_like", "like_count":like_count, 'disliked_video_id':disliked_video_id, 'dislike_count':dislike_count, "is_logged_in":is_logged_in}
                return HttpResponse(json.dumps(context))
        
        else:
            is_logged_in = is_logged_in
            context = {"is_logged_in":is_logged_in}
            return HttpResponse(json.dumps(context))


def dislike_video(request, id):
    if request.method == "POST":
        is_logged_in = False
        if request.user.is_authenticated:
            is_logged_in = True
            video_obj = Video.objects.get(id = id)
            try:
                disliked_obj = Dislike.objects.get(video = video_obj.id)
            except:
                disliked_obj = None

            try:
                liked_obj = Like.objects.get(video = video_obj.id)
            except:
                liked_obj = None


            if liked_obj:
                like_count = video_obj.like.user.count()
            else:
                like_count = 0

            liked_video_id = f"{id}_like"
            disliked = False
            if disliked_obj:
                if request.user in video_obj.dislike.user.all():
                    print("--------------------------------")
                    video_obj.dislike.user.remove(request.user)
                    video_obj.save()
                    dislike_count = video_obj.dislike.user.count()
                    disliked = False
                    context = {'disliked':disliked, 'video_id':f"{id}_dislike", "dislike_count":dislike_count, 'liked_video_id':liked_video_id, "like_count":like_count, "is_logged_in":is_logged_in}
                    return HttpResponse(json.dumps(context))
                
                else:
                    disliked_obj.user.add(request.user)
                    if liked_obj:
                        liked_obj.user.remove(request.user)
                        like_count = video_obj.like.user.count()
                    else:
                        like_count = like_count

                    dislike_count = video_obj.dislike.user.count()
                    disliked = True
                    context = {'disliked':disliked, 'video_id':f"{id}_dislike", "dislike_count":dislike_count, 'liked_video_id':liked_video_id, "like_count":like_count, "is_logged_in":is_logged_in}
                    return HttpResponse(json.dumps(context))
            else:
                print("=====================")
                
                dislike_obj = Dislike.objects.create(video = video_obj)
                dislike_obj.user.add(request.user)
                if liked_obj:
                    liked_obj.user.remove(request.user)
                    like_count = video_obj.like.user.count()
                else:
                    like_count = like_count
                dislike_count = video_obj.dislike.user.count()
                disliked = True
                context = {'disliked':disliked, 'video_id':f"{id}_dislike", "dislike_count":dislike_count, 'liked_video_id':liked_video_id, "like_count":like_count, "is_logged_in":is_logged_in}
                return HttpResponse(json.dumps(context))
        
        else:
            is_logged_in = is_logged_in
            print(is_logged_in)
            context = {"is_logged_in":is_logged_in}
            return HttpResponse(json.dumps(context))
        
        

    