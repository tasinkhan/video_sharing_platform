from django.contrib import admin
from .models import Video, Like, Dislike
# Register your models here.

admin.site.register(Video)
admin.site.register(Like)
admin.site.register(Dislike)