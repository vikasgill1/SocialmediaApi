
from functools import partial
from django.http import Http404
from rest_framework.status import *
from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView
from .serializers import *
from ..models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User



class Register(APIView):
    def get(self,request):
        stu=User.objects.all()
        serializer=UserSerializer(stu,many=True)

        return Response(serializer.data)

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
        # data=request.user  
        stu=Post.objects.create(user=request.user,) 
        serializer=PostSerializer(instance=stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'post successfull'})
        return Response(serializer.errors)

    def put(self,request):
        
        stu=Post.objects.get(user=request.user)
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

class likeView(APIView):
    def get(self,request):
        
        stu=Postlike.objects.filter(post=request.data.get('post'),like=True)
        count=str(stu.count())
        print(count)
        serializer=likeSerializer(stu,many=True)
        return Response({'data':serializer.data,'count':count})

class like(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request):
        stu,_=Postlike.objects.get_or_create(post_id=request.data.get('post'),user=request.user)
        if stu.like == True :
            stu.like = False
            stu.save()

            return Response('like')
        else:
            stu.like= True
            stu.save()
            return Response('unlike')


    
class CommentView(APIView):
    def get(self,request):
        data=request.data
        stu=Postcomment.objects.filter(post_id=data.get('post'))
        count=stu.count()
        serializer=likeSerializer(stu,many=True)
        return Response({'data':serializer.data,"comment":count})

        
class comment(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request):
        stu=Postcomment.objects.create(user=request.user)
        serialzer=PostSerializer(stu,data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'status': 'comment successfully in a post'})
        return Response(serialzer.errors)


    def put(self,request):
        user=request.user
        data=request.data
        stu=Postcomment.objects.filter(user=user,post_id=data.get('post'))
        serializer=UserSerializer(instance=stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'update successfull'})
        return Response({'status': serializer.errors})
    
    def delete(self,request):
        user=request.user
        data=request.data
        stu=User.objects.filter(user=user,post__id=data.get('post'))
        stu.delete()
        return Response({'status': 'your account delete successfull'})      


class SendRequest(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        stu=FriendRequest1.objects.filter(user_to=request.user,is_accept=False)
        serializer=FriendRequest1Serializer(stu,many=True)
        return Response(serializer.data)
    def post(self,request):
        stu,_=FriendRequest1.objects.get_or_create(user_to=request.user,user_from_id=request.data.get('user_from'))
        stu.save()
        return Response({'status': 'sendfriend Request'})

    def delete(self,request):
        try:
            stu=FriendRequest1.objects.filter(user_to=request.user,is_accept=False,user_form_id=request.data.get('user_from'))
            stu.delete()
            return Response({'status': 'sendfriend Request'})
        except:
            return Response({'status':'User does not exits'})

class AcceptRequest(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        stu=FriendRequest1.objects.filter(user_from=request.user,is_accept=False)
        serializer=FriendRequest1Serializer(stu,many=True)
        return Response(serializer.data)
    def put(self,request):
        try:
            stu=FriendRequest1.objects.get(user_from=request.user,is_accept=False,user_to_id=request.data.get('user_to'))
            stu.is_accept = True
            stu.save()
            return Response({'status':'accept request'})
        except Exception as e:
            return Response({'error':str(e)})
        

    def delete(self,request):
        try:
            stu=FriendRequest1.objects.filter(user_from=request.user,is_accept=False,user_to_id=request.data.get('user_to'))
            stu.delete()
            return Response({'status': 'Cancel friend Request'})
        except Exception as e:
            return Response({'status': str(e)})
        