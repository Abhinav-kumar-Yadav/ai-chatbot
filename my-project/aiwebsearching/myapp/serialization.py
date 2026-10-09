from rest_framework import serializers
from .models import Users




class User_Serializer(serializers.Serializer):
    model = Users
    feilds = ["email","password","date"]