from .models                   import *
from .serializers              import *
from rest_framework            import status
from django.shortcuts          import render
from rest_framework.response   import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

# ----- 1. GET and POST APIs to fetch a particular Movie, Add or Update a movie -----
@api_view(['GET', 'POST', 'PUT'])
def movie_detail(request, movie_id=None):
    # ----- Retrieve the movie details of a particular movie -----
    if request.method == 'GET':
        mov = movie.objects.filter(id=movie_id).first()
        if not mov:
            return Response({"Error": "Movie for the given ID is not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(mov)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # ----- Create a new movie instance -----
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ----- Update the movie details of a particular movie -----
    elif request.method == 'PUT':
        mov = movie.objects.filter(id=movie_id).first()
        if not mov:
            return Response({"Error": "Movie for the given ID is not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(mov, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----- 2. GET method to fetch all the movies paginated with custom filters -----
@api_view(['GET'])
def movies_list(request):
    paginator = PageNumberPagination()
    movies = movie.objects.all()
    actor_id = request.GET.get('actor_id')
    director_id = request.GET.get('director_id')
    producer_id = request.GET.get('producer_id')
    technician_id = request.GET.get('technician_id')
    # ----- Filtering movies of a particular actor -----
    if actor_id:
        movies = movies.filter(actors__id=actor_id)
    # ----- Filtering movies of a particular director -----
    if director_id:
        movies = movies.filter(directors__id=director_id)
    # ----- Filtering movies of a particular producer -----
    if producer_id:
        movies = movies.filter(producers__id=producer_id)
    # ----- Filtering movies of a particular technician -----
    if technician_id:
        movies = movies.filter(technicians__id=technician_id)
    # ----- Filtering movies of a combination of particular actor, director, producer, and technician -----
    if actor_id and director_id and producer_id and technician_id:
        movies = movies.filter(actors__id=actor_id,directors__id=director_id,producers__id=producer_id,technicians__id=technician_id)
    result_page = paginator.paginate_queryset(movies, request)
    serializer = MovieSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# ----- 3. POST API to delete an actor from the database if he or she is not associated with any movies -----
@api_view(['POST'])
def delete_actor(request, actor_id):
    act = actor.objects.filter(id=actor_id).first()
    if not act:
        return Response({"error": "Actor of given ID is not found."}, status=status.HTTP_404_NOT_FOUND)
    if act.movies.all().exists():
        return Response({"error": "Sorry can't perform deletion. The Actor of given ID is associated with some movies."}, status=status.HTTP_400_BAD_REQUEST)
    act.delete()
    return Response({"message": "The Actor of given ID is not associated with any movie. Hence, the actor is deleted successfully"}, status=status.HTTP_200_OK)