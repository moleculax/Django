from django.urls import path

# from movie.views import get_movies, put_movies
from movie.views import VistaMovie, MovieList, MovieBYID

app_name = "movie"

urlpatterns = [
    path("", VistaMovie.as_view(), name="movie"),
    path("list", MovieList.as_view(), name="movie_list"),
    path("list/<int:pk>", MovieBYID.as_view(), name="movie_list_id"),

    # path("", get_movies, name="movie"),
    # path("<int:pk>", put_movies, name="movie"),
]
