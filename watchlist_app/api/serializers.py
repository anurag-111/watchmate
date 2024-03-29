from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


# Model Serialization

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = "__all__"
  
class WatchListSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many = True, read_only = True)
  
  class Meta:
    model = WatchList
    fields = "__all__"

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
  watchlist = WatchListSerializer(many = True, read_only = True)
  
  class Meta:
    model = StreamPlatform
    fields = "__all__"
  
  # For particular string field to be serialized
  # watchlist = serializers.StringRelatedField(many = True)
  
  # Hyperlink : used to represent the target of the relationship.
  # watchlist = serializers.HyperlinkedRelatedField(
  #       many=True,
  #       read_only=True,
  #       view_name='movie-details'
  #   )
  
  # def get_len_name(self, object):
  #   length = len(object.name)
  #   return length
    
  # def validate(self, data):
  #   if data['name'] == data['description']:
  #     raise serializers.ValidationError("Title and description should be different!")
  #   else:
  #     return data
    
  # def validate_name(self, value):
  #   if len(value) < 2:
  #     raise serializers.ValidationError("Movie name is too short!")
  #   else:
  #     return value
    
# def name_length(value):
#   if len(value) < 2:
#     raise serializers.ValidationError("Movie name is too short!")
#   else:
#     return value
  
# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only = True)
#   name = serializers.CharField(validators = [name_length]) # 1. Validators
#   description = serializers.CharField()
#   active = serializers.BooleanField()
  
#   def create(self, validated_data):
#     return Movie.objects.create(**validated_data)
  
#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.description = validated_data.get('description', instance.description)
#     instance.active = validated_data.get('active', instance.active)
#     instance.save()
#     return instance
  
#   # 2. Object level validators 
#   def validate(self, data):
#     if data['name'] == data['description']:
#       raise serializers.ValidationError("Title and description should be different!")
#     else:
#       return data
    
  # 3. Field level validators  
  # def validate_name(self, value):
  #   if len(value) < 2:
  #     raise serializers.ValidationError("Movie name is too short!")
  #   else:
  #     return value