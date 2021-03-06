from django.conf.urls import url
from .views import (AddEmpAPIView,GetEmployeeListAPIView,DeleteEmpAPIView,UpdateEmpAPIView,getEmpDetailsAPIView)
urlpatterns=[
    url('add',AddEmpAPIView.as_view()),
    url('getEmployee',GetEmployeeListAPIView.as_view()),
    url('deleteEmp/(?P<pk>.+)',DeleteEmpAPIView.as_view()),
    url('getEmpDetails/(?P<pk>.+)',getEmpDetailsAPIView.as_view()),
    url('updateEmp/(?P<pk>.+)', UpdateEmpAPIView.as_view())

]