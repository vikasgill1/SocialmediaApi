from django.contrib import admin

from application.models import Post, Postcomment, Postlike, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Postlike)
admin.site.register(Postcomment)
