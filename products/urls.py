from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductView)
router.register('producttypes', views.ProductTypeView)
router.register('customers', views.CustomerView)

urlpatterns = [
    path('', include(router.urls)),
]