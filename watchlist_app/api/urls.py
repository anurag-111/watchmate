from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view()),
    path('<int:pk>', WatchDetailAV.as_view()),
    path('stream/list/', StreamPlatformAV.as_view(),  name='streamplatform-list'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='streamplatform-detail')     
]
