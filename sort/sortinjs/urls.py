from django.urls import path

from .import views

urlpatterns=[
    path("example1/",views.createfirst)
]