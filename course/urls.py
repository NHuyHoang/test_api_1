from django.urls import path
from .views import CourseList
urlpatterns = [
    path(r'courses/', CourseList.as_view())
]
