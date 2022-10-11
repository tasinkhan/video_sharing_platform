from django.db import models
from users.models import User
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length = 255)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.title
