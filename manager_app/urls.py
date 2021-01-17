from django.conf.urls import url
from .views import (UserSignUpAPIView,UserLoginAPIView)

urlpatterns =[
    url('signup', UserSignUpAPIView.as_view()),
    url('signin',UserLoginAPIView.as_view())
]