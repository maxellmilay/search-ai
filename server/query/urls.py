from django.urls import path
from .views import CreateQuery

urlpatterns = [
    path("",CreateQuery, name="Create Query")
]

