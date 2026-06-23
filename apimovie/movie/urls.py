from django.urls import path
from movie.views import VistaMovie, MovieList, MovieBYID, MovieCreate, MovieUpdate, MovieDelete, MovieBYIDUSUARIO

app_name = "movie"

urlpatterns = [
    # path("", VistaMovie.as_view(), name="movie"),
    # path("list", MovieList.as_view(), name="movie_list"),
    path("", MovieList.as_view(), name="movie_list"),
    path("create/", MovieCreate.as_view(), name="movie-create"),  # ← MOVER ANTES DE <int:pk>
    path("<int:pk>/", MovieBYID.as_view(), name="movie_list_id"),
    path("user/<int:user_id>/", MovieBYIDUSUARIO.as_view(), name="movie_by_user"),
    path("update/<int:pk>/", MovieUpdate.as_view(), name="movie-update"),
    path("delete/<int:pk>/", MovieDelete.as_view(), name="movie-delete"),

    # path("", get_movies, name="movie"),
    # path("<int:pk>", put_movies, name="movie"),
]