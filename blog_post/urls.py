from django.urls import path
from .views import post_detail, post_list
urlpatterns = [
    path(r'blogs/', post_list.as_view(), name='blog-list'),
    path('blogs/<str:pk>/', post_detail.as_view(), name='blog-detail')
]
