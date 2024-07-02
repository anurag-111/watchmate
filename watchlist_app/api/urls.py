from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, StreamPlatformAV,
                                     StreamPlatformVS, ReviewList, ReviewDetail, ReviewCreate)

#  TheReviewDetail, AllReviewList
router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view()),
    path('<int:pk>', WatchDetailAV.as_view()),
    # path('stream/', StreamPlatformAV.as_view(),  name='streamplatform-list'),
    # path('stream/<int:pk>', StreamPlatformVS.as_view({'get': 'retrieve', 
    #                                                   'put': 'update', 
    #                                                   'delete': 'destroy'}), name='streamplatform-detail'),
    path('', include(router.urls)),
    # path('review/', AllReviewList.as_view(), name = 'review-list'),
    # path('review/<int:pk>', TheReviewDetail.as_view(), name = 'review-detail'),
    path('list/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('list/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('list/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
