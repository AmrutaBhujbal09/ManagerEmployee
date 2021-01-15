from rest_framework import serializers
from .models import Employee




class AddEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=["id","first_name","last_name","email","password",
                "user_id","address","dob","company","city","mobile"]

class UpdateEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id","first_name","last_name","address","mobile","dob","company","city"]


