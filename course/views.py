from django.shortcuts import render
from django.core import serializers
from rest_framework import generics
from student.models import Student
from .serializers import CourseSerializer
from .models import Course
from django.core import serializers
from .models import Course
from rest_framework.response import Response

class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self,request):
        queryset = self.get_queryset()
        print(type(request.user))
        serializer = CourseSerializer(queryset,many=True)
        courses = serializer.data
        res = {}
        for course in courses:
            data = {}
            student_ids = course['register']
            data = dict(course)
            students = list(map(lambda student_id: Student.objects.get(id=student_id).to_json(), list(student_ids)))
            data['register'] = students
            res[course['id']] = data
        return Response(res)
