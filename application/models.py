from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='application/post_image')
    describe=models.TextField(max_length=200)
    

class Postlike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    like=models.BooleanField(default=False)

class Postcomment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField(max_length=999)

class FriendRequest(models.Model):
    to_user=models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)
    from_user=models.ForeignKey(User,related_name='from_user',on_delete=models.CASCADE)
    is_accept=models.BooleanField(default=False)
