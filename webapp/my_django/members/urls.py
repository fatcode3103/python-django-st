from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("members/", views.members, name="members"),
    path("members/details/<int:id>", views.details_member, name="details"),
    path("testing/", views.testing, name="testing"),
]
