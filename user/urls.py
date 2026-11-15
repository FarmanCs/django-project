from django.urls import path
from . import views

urlpatterns = [
    path("", views.userindex, name="userindex"),
    path(
        "subject/",
        views.user_subject,
        name="user_subject",
    ),
]
