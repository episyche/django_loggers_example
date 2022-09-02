from django.urls import path

from .views import *

urlpatterns = [
    path('example/', Example_API.as_view()),
]