from django.urls import path, include
from .views import post_detail, post_list, post_viewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'viewset', post_viewset)

urlpatterns = [
    path(r'blogs/', post_list.as_view(), name='blog-list'),
    path(r'blogs/', include(router.urls)),
    path('blog/<str:id>/', post_detail.as_view()),
    # path('blog/<str:title>/', post_detail.as_view()),
    
    
    # path('blogs/<str:title>/<str:content>', post_detail.as_view(), name='blog-detail'),
    
]
