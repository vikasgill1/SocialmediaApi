from dataclasses import field
from ..models import *
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=("__all__")
        
class PostSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=('__all__')

class likeSerializer(ModelSerializer):

    class Meta:
        model=Postlike
        fields=('__all__')

class CommentSerializer(ModelSerializer):
    class Meta:
        model=Postcomment
        fields=('__all__')



class FriendRequest1Serializer(ModelSerializer):
    class Meta:
        model=FriendRequest1
        fields=('__all__')