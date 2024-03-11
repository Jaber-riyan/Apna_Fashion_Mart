from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('list',ProductViewset)
router.register('chartList',ChartViewset)

urlpatterns = [
    path('',include(router.urls)),
]


