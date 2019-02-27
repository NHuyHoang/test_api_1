from rest_framework import generics, permissions, renderers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Post
from django.contrib.auth.models import User
from .serializers import post_serializer, user_serializer
from .permissions import IsOwnerOrReadOnly


class post_list(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-id')
    serializer_class = post_serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(userId = self.request.user)

class post_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = post_serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.something_new = 'new value'
        serializer = post_serializer(post)
        return Response(serializer.data)

class post_body(generics.GenericAPIView): # new
    queryset = Post.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.body)    

class user_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer

class user_detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer

@api_view(['GET', 'POST'])
def api_root(request,format=None):
    if(request.method == 'POST'):
        serializer = post_serializer(data = request.data)
        if serializer.is_valid():
            print('valid')
        else:
            print('not valid')
            print(serializer.errors)
        return Response({
           'success':True,
           'data':request.data
        })

    else:
        return Response({
            'users': reverse('user-list', request=request, format=format),
            'posts': reverse('post-list', request=request, format=format),
        })
