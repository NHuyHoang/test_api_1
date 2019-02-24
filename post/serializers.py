from rest_framework import serializers
from .models import Post

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('userId','id','title','body')

