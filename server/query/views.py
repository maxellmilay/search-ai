from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Query
from .serializers import QuerySerializer

class CreateQuery(ListCreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
