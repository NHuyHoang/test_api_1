from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student
# Create your views here.

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

