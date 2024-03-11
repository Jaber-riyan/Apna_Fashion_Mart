from django.shortcuts import render
from rest_framework import viewsets
from .models import CategoryModel
from .serializers import CategorySerializer

# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        print(self.request.query_params)
        category_id = self.request.query_params.get('category_id')
        print(category_id)
        if category_id:
            category_id = category_id.rstrip('/')
            queryset = queryset.filter(id=category_id)
        return queryset