
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import *
from ..models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User



class Register(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']
        user=User(username=username)
        user.set_password(password)
        
        user.save()
        refresh=RefreshToken.for_user(user)
        return Response({'status':'success register','refresh token':str(refresh),'access token' : str(refresh.access_token)})

class Profile(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user=request.user
        print(user)
        stu=User.objects.filter(id=user.id)
        serializers=UserSerializer(stu,many=True)
        return Response(serializers.data)

    def put(self,request):
        user=request.user
        stu=User.objects.filter(id=user.id)
        serializer=UserSerializer(instance=stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'update successfull'})
        return Response({'status': serializer.errors})
    
    def delete(self,request):
        user=request.user
        stu=User.objects.filter(id=user.id)
        stu.delete()
        return Response({'status': 'your account delete successfull'})

class PostView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        user=request.user
        stu=Post.objects.filter(user=user)
        serializer=PostSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        user=request.user
        serializer=PostSerializer(user=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'post successfull'})
        return Response(serializer.errors)

    def put(self,request):
        user=request.user
        stu=Post.objects.filter(user=user)
        seriailizer=PostSerializer(instance=stu,data=request.data)
        if seriailizer.is_valid():
            seriailizer.save()
            return Response({'status':'update successful'})
        return Response(seriailizer.errors)

    def delete(self,request):
        user=request.user
        data=request.data
        stu=Post.objects.filter(id=data.get('id'),user=user)
        stu.delete()
        return Response('delete succesfully')

class Postlike(APIView):
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        data=request.data
        stu=Postlike.objects.filter(post__id=data.get('post'),like=True)
        serializer=likeSerializer(stu,many=True)
        return Response(serializer.data)
    def post(self,request):
        
        user=request.user
        data=request.data
        stu=Postlike.objects.get_or_create(post__id=data.get('post'),user=user)
        if stu.like == True :
            stu.like = False
            stu.save()

            return Response('like')
        else:
            stu.like= True
            stu.save()
            return Response('unlike')

class Postcomment(APIView):


        


        
