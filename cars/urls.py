from django.urls import path 
from .views import BrandDetailView, BrandsView

urlpatterns = [
    path('', BrandsView.as_view(), name='brands'),
    path('<int:pk>/', BrandDetailView.as_view(), name='brand')
]