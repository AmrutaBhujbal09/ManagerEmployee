from rest_framework import status
from rest_framework.generics import(GenericAPIView,CreateAPIView)
from rest_framework.response import Response
from .serializers import (UserSignUpSerializer, UserLoginSerializer)
from .models import User




class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def post(self,request, *args, **kwargs):
        print("REQUEST_DATA",request.data)
        serialize=self.get_serializer(data=request.data)

        if serialize.is_valid():
            serialize.save()
            obj=User.objects.get(email=request.data["email"])

            response_data={
                "id":obj.id,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
                "email-address":obj.email
            }

            return Response(response_data)
        else:
            return Response(serialize.errors)


class UserLoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print("Request data:", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.Userval

            response_data = {
                "id": obj.id,
                "first_name": obj.first_name,
                "last_name": obj.last_name,
                "email-AAddress": obj.email
            }

            return Response(response_data)
        else:
            return Response(serializer.errors)
