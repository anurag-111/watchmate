from rest_framework.response import Response
from rest_framework import status, viewsets
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics

from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

# Class-based views
class StreamPlatformVS(viewsets.ModelViewSet):
  queryset = StreamPlatform.objects.all()
  serializer_class = StreamPlatformSerializer


class ReviewCreate(generics.CreateAPIView):
  serializer_class = ReviewSerializer
  
  def perform_create(self, serializer):
    # Retrieves the value of the pk (primary key) from the URL kwargs (self.kwargs). 
    # In Django, self.kwargs contains all the keyword arguments captured in the URL pattern.
    watchlist_pk = self.kwargs.get('pk')
    # Retrieves the WatchList object from the database using the primary key (pk) obtained 
    # from the URL kwargs. It uses WatchList.objects.get() to fetch the object based on the primary key.
    watchlist_instance = WatchList.objects.get(pk = watchlist_pk)
    serializer.save(watchlist = watchlist_instance)    
  
class ReviewList(generics.ListAPIView):
  # queryset = Review.objects.all() 
  serializer_class = ReviewSerializer
  
  # Overriding the queryset
  def get_queryset(self):
    pk = self.kwargs['pk']
    return Review.objects.filter(watchlist=pk)
  
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

# class TheReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializer
  
#   def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class AllReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class WatchListAV(APIView):
  def get(self, request):
    watchlist = WatchList.objects.all()
    serializer = WatchListSerializer(watchlist, many = True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = WatchListSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

class WatchDetailAV(APIView):
  def get(self, request, pk):
    try:
      movie = WatchList.objects.get(pk = pk)
    except WatchList.DoesNotExist:
      return Response({'Error' : 'Movie not found'} , status = status.HTTP_404_NOT_FOUND)
      
    serializer = WatchListSerializer(movie)
    return Response(serializer.data)
  
  def put(self, request, pk):
    movie = WatchList.objects.get(pk = pk)
    serializer = WatchListSerializer(movie,data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  
  def delete(self, request,pk):
    movie = WatchList.objects.get(pk = pk)
    movie.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)

class StreamPlatformAV(APIView):
  def get(self, request):
    streams = StreamPlatform.objects.all()
    serializer = StreamPlatformSerializer(streams, many = True, context={'request': request})
    return Response(serializer.data)
  
  def post(self, request):
    serializer = StreamPlatformSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

# class StreamPlatformDetailAV(APIView):
  
#   def get(self, request, pk):
#     try:
#       stream = StreamPlatform.objects.get(pk = pk)
#     except StreamPlatform.DoesNotExist:
#       return Response({'Error' : 'Stream not found'} , status = status.HTTP_404_NOT_FOUND)
    
#     serializer = StreamPlatformSerializer(stream, context={'request': request})
#     return Response(serializer.data)
  
#   def put(self, request, pk):
#     stream = StreamPlatform.objects.get(pk = pk)
#     serializer = StreamPlatformSerializer(stream, data = request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)
  
#   def delete(self, request,pk):
#     stream = StreamPlatform.objects.get(pk = pk)
#     stream.delete()
#     return Response(status = status.HTTP_204_NO_CONTENT)
    
# Function-based views
# @api_view(['GET', 'POST'])
# def movie_list(request):
  
#   if request.method == 'GET':
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many = True)
#     return Response(serializer.data)
  
#   if request.method == 'POST':
#     serializer = MovieSerializer(data = request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)
  
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
  
#   if request.method == 'GET':
#     try:
#       movie = Movie.objects.get(pk = pk)
#     except Movie.DoesNotExist:
#       return Response({'Error' : 'Movie not found'} , status = status.HTTP_404_NOT_FOUND)
      
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)
  
#   if request.method == 'PUT':
#     movie = Movie.objects.get(pk = pk)
#     serializer = MovieSerializer(movie,data = request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)
      
#   if request.method == 'DELETE':
#     movie = Movie.objects.get(pk = pk)
#     movie.delete()
#     return Response(status = status.HTTP_204_NO_CONTENT)
