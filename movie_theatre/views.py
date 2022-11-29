from django.shortcuts import render, get_object_or_404
from movie_theatre.serializers import MovieSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie

# Create your views here.
#localhost:3000/movies/ get post
class MoviesView(APIView):
    """View class for movies/ for viewing all and creating"""
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response({'movies': serializer.data})

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:3000/movies/:id get delete update
class MovieDetailView(APIView):
    """View class for movies/:pk for viewing a single movie, updating a single movie, or removing a single movie"""
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response({'movie': serializer.data})

    def patch(self, request, pk):
        Movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


