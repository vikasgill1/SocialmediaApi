from django.contrib import admin

from application.models import  FriendRequest1, Post, Postcomment, Postlike, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Postlike)
admin.site.register(Postcomment)

admin.site.register(FriendRequest1)