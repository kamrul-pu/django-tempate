"""Urls mappings for users."""
from django.urls import path

from core.rest.views.user import UserList, UserDetail

urlpatterns = [
    path("", UserList.as_view(), name="user-list"),
    path("/<int:pk>", UserDetail.as_view(), name="user-details"),
]
