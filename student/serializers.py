from rest_framework import serializers
from .models import Student
from course.models import Course
from course.serializers import CourseSerializer


class StudentSerializer(serializers.ModelSerializer):
    #courses = serializers.RelatedField(source='course', read_only=True)
    # courses = serializers.PrimaryKeyRelatedField(
    #     queryset=Course.objects.all(), many=True)

    #course = serializers.ManyRelatedField(child_relation=Course.objects.all())
    courses = CourseSerializer(many=True, read_only= True)

    class Meta:
        model = Student
        fields = ('id', 'name', 'courses')
