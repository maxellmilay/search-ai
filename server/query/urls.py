from django.urls import path
from .views import search_query

urlpatterns = [
    path("search", search_query, name="AI Search")
]

