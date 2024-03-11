from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        print(self.request.query_params)
        category_id = self.request.query_params.get('category_id')
        print(category_id)
        if category_id:
            category_id = category_id.rstrip('/')
            queryset = queryset.filter(category=category_id)
        return queryset
    


   
class ChartViewset(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            user_id = user_id.rstrip('/')
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
    
    def delete(self, chart_id):
        try:
            delete_chart = Chart.objects.get(pk=chart_id)
            delete_chart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Chart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        