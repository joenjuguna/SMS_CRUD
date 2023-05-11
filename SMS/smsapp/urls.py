from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .views import smsAPI
router = DefaultRouter()
router.register(r'sms',smsAPI)

urlpatterns = [
    path('index',views.create,name="index" ),
    path('readone', views.readone, name="readone"),
    path('readall', views.readall, name="readall"),
    path('delete', views.delete, name="delete"),
    path('update', views.update, name="update"),
    path('', include(router.urls)),
]