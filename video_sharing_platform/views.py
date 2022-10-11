from django.shortcuts import render
from django.http import HttpResponse
from video.models import Video


def index(request):
    video_queryset = Video.objects.all()
    return render(request, "list.html", context={"videos":video_queryset})

