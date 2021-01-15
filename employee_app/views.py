from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import(GenericAPIView,CreateAPIView,ListAPIView,DestroyAPIView,UpdateAPIView)
from rest_framework.response import Response
from .serializers import (AddEmpSerializer,UpdateEmpSerializer)
from .models import Employee

class AddEmpAPIView(CreateAPIView):
    serializer_class = AddEmpSerializer
    # post is a HTTP method.You can used this method during creating/inserting data.
    def post(self,request, *args, **kwargs):
        print("REQUEST_DATA",request.data)
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            #.save() method will either create a new model instance or update excisting instance.
        return Response(serializer.data,status.HTTP_201_CREATED)





class GetEmployeeListAPIView(ListAPIView):
    serializer_class=AddEmpSerializer
   # get is a HTTP method.You can used this method during retriving data/getting data i.e reading data.
    def get_queryset(self):
        return Employee.objects.filter()
    #get_queryset() used by ListViews it determines the list of objects that you want to display.By default it will give you all for the model you spcify.By overriding this method you can extend or replace logic.
    def get(selfself,request,*args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        print("SERIALIZER",serializer.data)
        return Response(serializer.data,status.HTTP_200_OK)

class DeleteEmpAPIView(DestroyAPIView):
    def delete(self,request, *args, **kwargs):
        user_id = self.kwargs["pk"]
        Employee.objects.filter(id=user_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)
    # delete() is HTPP mrthod .You can use this method for deleting data.

class UpdateEmpAPIView(UpdateAPIView):
    serializer_class=UpdateEmpSerializer

    def get_queryset(self):
        user_id=self.kwargs['pk']
        return Employee.objects.filter(id=user_id)

    def patch(self,request,  *args,  **kwargs):
        instance=self.get_object()
    # patch() is a HTTP method.You can used this method for updating the data.

        instance.address=request.data["address"]
        instance.first_name=request.data["first_name"]
        instance.last_name=request.data["last_name"]
        instance.mobile= request.data["mobile"]
        instance.city = request.data["city"]
        instance.dob=request.data["dob"]
        instance.company=request.data["company"]
        serializer = self.get_serializer(instance,data=request.data)
        """
        return the serializer instance that should be used for validating and deserializing input and serializing output
        """
        if serializer.is_valid(raise_exception=True):
            self.partial_update(serializer)

        return Response(serializer.data,status.HTTP_200_OK)


