from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import(GenericAPIView,CreateAPIView,ListAPIView,DestroyAPIView,UpdateAPIView)
from rest_framework.response import Response
from .serializers import (AddEmpSerializer,UpdateEmpSerializer)
from .models import Employee

class AddEmpAPIView(CreateAPIView):
    serializer_class = AddEmpSerializer

    def post(self,request, *args, **kwargs):
        print("REQUEST_DATA",request.data)
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data,status.HTTP_201_CREATED)





class GetEmployeeListAPIView(ListAPIView):
    serializer_class=AddEmpSerializer

    def get_queryset(self):
        return Employee.objects.filter()

    def get(selfself,request,*args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        print("SERIALIZER",serializer.data)
        return Response(serializer.data,status.HTTP_200_OK)

class DeleteEmpAPIView(DestroyAPIView):
    def delete(self,request, *args, **kwargs):
        user_id = self.kwargs["pk"]
        Employee.objects.filter(id=user_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)


class UpdateEmpAPIView(UpdateAPIView):
    serializer_class=UpdateEmpSerializer

    def get_queryset(self):
        user_id=self.kwargs['pk']
        return Employee.objects.filter(id=user_id)

    def patch(self,request,  *args,  **kwargs):
        instance=self.get_object()


        instance.address=request.data["address"]
        instance.first_name=request.data["first_name"]
        instance.last_name=request.data["last_name"]
        instance.mobile= request.data["mobile"]
        #nstance.email = request.data["email"]
        instance.city = request.data["city"]
        instance.dob=request.data["dob"]
        instance.company=request.data["company"]
        serializer = self.get_serializer(instance,data=request.data)
        #given data to serializer for validation...


        if serializer.is_valid(raise_exception=True):
            self.partial_update(serializer)

        return Response(serializer.data,status.HTTP_200_OK)


