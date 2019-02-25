from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

urlpatterns = [
    path('posts/', views.post_list.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.post_detail.as_view()),
    path('posts/<int:pk>/body/',
         views.post_body.as_view(), name='post_body'),

    path('users/', views.user_list.as_view(), name='user-list'),
    path('users/<int:pk>/', views.user_detail.as_view()),
    path('auth/', include('rest_framework.urls')),

    path('', views.api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)