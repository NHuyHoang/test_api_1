from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

urlpatterns = [
    path('posts/', views.post_list.as_view()),
    path('posts/<int:pk>/', views.post_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)