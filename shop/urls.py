from django.urls import path
from .views import MembershipList, GroupList, CustomerList
urlpatterns = [
    path(r'customers/', CustomerList.as_view()),
    path(r'groups/', GroupList.as_view()),
    path(r'memberships/', MembershipList.as_view()),
]
