from django.urls import path
from .views import StudentList
urlpatterns = [
    path(r'students/', StudentList.as_view())
]
