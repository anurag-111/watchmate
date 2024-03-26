from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import MovieListAV, MovieDetailsAV, StreamPlatformListAV, StreamPlatformDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name = 'movie-list'),
    path('<int:pk>', MovieDetailsAV.as_view(), name = 'movie-details'),
    path('stream/list/', StreamPlatformListAV.as_view(), name = 'stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name = 'stream-details'),
]


def get_name(first_name: str, last_name: str):
    return first_name.append(" ").append(last_name)




get_name(last_name="bsrthesl", first_name="anurag")