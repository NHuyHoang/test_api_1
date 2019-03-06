from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=256)
    customers = models.ManyToManyField(Customer,  through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='groups')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)