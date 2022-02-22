from dataclasses import field
from ..models import *
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=("__all__")
        
class PostSerializer(ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Post
        fields=('__all__')

class likeSerializer(ModelSerializer):
    user=UserSerializer()
    post=PostSerializer()
    class Meta:
        model=Postlike
        fields=('__all__')

class CommentSerializer(ModelSerializer):
    user=UserSerializer()
    post=PostSerializer()
    class Meta:
        model=Postcomment
        fields=('__all__')

