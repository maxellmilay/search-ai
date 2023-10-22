from django.urls import path
from .views import CreateQuery

urlpatterns = [
    path("",CreateQuery.as_view(), name="Create Query")
]

