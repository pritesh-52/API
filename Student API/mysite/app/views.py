from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .models import Student
from rest_framework import viewsets
from  .Serializers import Studentserilzer
# Create your views here.

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


class Studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class =Studentserilzer
