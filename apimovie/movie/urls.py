from django.urls import path

# from movie.views import get_movies, put_movies
from movie.views import VistaMovie, MovieList, MovieBYID, MovieCreate, MovieUpdate, MovieDelete

app_name = "movie"

urlpatterns = [
    # path("", VistaMovie.as_view(), name="movie"),
    # path("list", MovieList.as_view(), name="movie_list"),
    path("listmovie/", MovieList.as_view(), name="movie_list"),
    path("listmovie/<int:pk>", MovieBYID.as_view(), name="movie_list_id"),
    path("createmovie/", MovieCreate.as_view(), name="movie-create"),
    path("updatemovie/<int:pk>", MovieUpdate.as_view(), name="movie-update"),
    path("deletemovie/<int:pk>", MovieDelete.as_view(), name="movie-delete"),

    # path("", get_movies, name="movie"),
    # path("<int:pk>", put_movies, name="movie"),
]
