from django.contrib import admin
from .models import Customer, Membership, Group
# Register your models here.
admin.site.register(Customer)
admin.site.register(Membership)
admin.site.register(Group)