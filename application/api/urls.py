from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
TokenVerifyView
)

urlpatterns = [
    path('userReg/',Register.as_view()),
    path('userprofile/',Profile.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('post/',PostView.as_view()),
    path('likeview/',likeView.as_view()),
    path('like/',like.as_view()),
    path('commentView',CommentView.as_view()),
    path('comment',comment.as_view()),
    path('sendRequest',SendFriendRequest.as_view()),
    path('acceptRequest',AcceptFriendRequest.as_view())
]