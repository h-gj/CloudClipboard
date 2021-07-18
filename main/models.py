from django.db import models

# Create your models here.


class Channel(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)
    creator_ip = models.GenericIPAddressField(null=True)


class ClipBoardContent(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)
    publish_ip = models.GenericIPAddressField()