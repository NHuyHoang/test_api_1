from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomerSerializer, MembershipSerializer, GroupSerializer
from .models import Customer, Membership, Group

class CustomerList(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class MembershipList(generics.ListAPIView):
    serializer_class = MembershipSerializer
    queryset = Membership.objects.all()

class GroupList(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()