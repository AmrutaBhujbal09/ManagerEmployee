from django.conf.urls import url
from .views import (UserSignUpAPIView,UserLoginAPIView)

urlpatterns =[
    url('signup', UserSignUpAPIView.as_view()),
    url('login',UserLoginAPIView.as_view())
]