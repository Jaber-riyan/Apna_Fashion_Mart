from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewset,UserRegistrationApiView, UserLoginApiView,UserLogoutView,activate


router = DefaultRouter()
router.register('list',UserViewset)


urlpatterns = [
    path('',include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/',UserLogoutView.as_view(), name='logout'),
    path('activate/<uid64>/<token>/', activate, name = 'activate'),
]
