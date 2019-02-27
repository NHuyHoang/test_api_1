from rest_framework import serializers
from .models import Course
#from student.serializers import StudentSerializer


class CourseSerializer(serializers.ModelSerializer):
    #register = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'date_start', 'date_end')
