from rest_framework import generics
from .models import Post
from .serializers import post_serializer

class post_list(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = post_serializer

class post_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = post_serializer


