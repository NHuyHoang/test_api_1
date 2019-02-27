from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class post_serializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=False, queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('userId', 'id', 'title', 'body')


class user_serializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
