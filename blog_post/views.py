from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import BlogPost
from .serializer import BlogSerializer

class post_list(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class post_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class post_viewset(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer