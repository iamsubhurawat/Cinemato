from .           import views
from django.urls import path

urlpatterns = [
    path('movies/',                views.movies_list,  name='movies_list'),
    path('movie/<int:movie_id>/',  views.movie_detail, name='movie_detail'),
    path('actors/<int:actor_id>/', views.delete_actor, name='delete_actor'),
]
