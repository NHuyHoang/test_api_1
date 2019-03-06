from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BlogPost
from .serializer import BlogSerializer
from django.shortcuts import get_object_or_404
from functools import reduce
from operator import or_
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework_simplejwt.authentication import JWTAuthentication


class post_list(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer


class MultiKeyGetObject(generics.GenericAPIView):
    def __init__(self):
        if not hasattr(self, 'lookup_fields'):
            raise AssertionError("Expected view {} to have `.lookup_fields` attribute".format(
                self.__class__.__name__))

    def get_object(self):
        print(self.kwargs)
        for field in self.lookup_fields:
            if field in self.kwargs:
                self.lookup_field = field
                break
        else:
            raise AssertionError(
                'Expected view %s to be called with one of the lookup_fields: %s' %
                (self.__class__.__name__, self.lookup_fields))

        return super().get_object()


class post_detail(MultiKeyGetObject, generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    lookup_fields = ('title', 'id')

class post_viewset(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    user = User.objects.get(username='huyhoang')
    #authentication_classes = ([],)
    #permission_classes = ([],)

    #@login_required() 
    #@permission_required('Can view blog post')
    @action(detail=True, methods=['get'])
    def change_title(self, request, pk=None):
        blog = self.get_object()
        # print(blog)
        # if 'title' in request.data:
        #     blog.title = request.data['title']
        #     blog.save()
        return Response(model_to_dict(blog))