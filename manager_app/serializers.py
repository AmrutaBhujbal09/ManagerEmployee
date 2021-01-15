
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","password","email","username","address","dob","company",
                "Status_Choice"]


    def create(self,validated_data):
        userval=User.objects.create_user(
           first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            password=validated_data.pop('password'),
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            address=validated_data.pop('address'),
            dob=validated_data.pop('dob'),
            company=validated_data.pop('company'),
            Status_Choice=validated_data.pop('Status_Choice')
        )
        return userval


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


    def validate(self,attrs):
        self.Userval=authenticate(username=attrs.pop("email"),password=attrs.pop("password"))

        #authenticate() takes two arguments username & password it returns ther user object if password is valid .It returns None if password is invalid.


        if self.Userval:
            return attrs

        else:
            raise serializers.ValidationError()


