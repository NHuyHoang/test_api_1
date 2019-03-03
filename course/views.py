from django.shortcuts import render
from rest_framework import generics
from .serializers import CourseSerializer
from .models import Course

class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
