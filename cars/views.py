from django.shortcuts import render

# Create your views here.
from car.serializers import BrandSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Brand

# Create your views here.
#localhost:3000/brands/ get post
class BrandsView(APIView):
    """View class for brands/ for viewing all and creating"""
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response({'brands': serializer.data})

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:3000/brands/:id get delete update
class BrandDetailView(APIView):
    """View class for brands/:pk for viewing a single brand, updating a single brand, or removing a single brand"""
    def get(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        serializer = BrandSerializer(brand)
        return Response({'brand': serializer.data})

    def patch(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)