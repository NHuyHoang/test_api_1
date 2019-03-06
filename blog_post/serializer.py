from rest_framework import serializers
from django.forms.models import model_to_dict
from .models import BlogPost

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')
        model = BlogPost
    
    def to_json(self):
        return model_to_dict( self )