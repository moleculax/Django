from django.urls import path
from movie.views import  MovieList, MovieBYID, MovieCreate, MovieUpdate, MovieDelete, MovieBYIDUSUARIO

app_name = "movie"

urlpatterns = [
    path("movies/", MovieList.as_view(), name="movie_list"),
    path("create/", MovieCreate.as_view(), name="movie-create"),
    path("<int:pk>/", MovieBYID.as_view(), name="movie_list_id"),
    path("user/<int:user_id>/", MovieBYIDUSUARIO.as_view(), name="movie_by_user"),
    path("update/<int:pk>/", MovieUpdate.as_view(), name="movie-update"),
    path("delete/<int:pk>/", MovieDelete.as_view(), name="movie-delete"),
]