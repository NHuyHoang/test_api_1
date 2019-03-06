import json
from rest_framework import serializers
from .models import Customer, Group, Membership
from django.forms.models import model_to_dict


class MembershipSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='group.name')
    id = serializers.ReadOnlyField(source='group.id')
    
    class Meta:
        model = Membership
        fields = ('name', 'id')

class CustomerSerializer(serializers.ModelSerializer):
    groups = MembershipSerializer(many=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'groups')


class CustomersField(serializers.RelatedField):
    queryset=Customer.objects.all()
    
    def to_representation(self, value):
        dict_obj = model_to_dict(value)
        return dict_obj
     
class GroupSerializer(serializers.ModelSerializer):
    customers = CustomersField(many=True)
    
    class Meta:
        model = Group
        fields = ('id', 'name', 'customers')

