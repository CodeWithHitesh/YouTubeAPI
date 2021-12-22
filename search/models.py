from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=100000)
    publishedAt = models.DateTimeField()
    video_id = models.CharField(max_length=1000)
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200)
    duration = models.IntegerField()
    thumbnail = models.CharField(max_length=1000)
