from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Models
class StreamPlatform(models.Model):
  platform_name = models.CharField(max_length = 30)
  platform_description = models.CharField(max_length = 100)
  platform_website = models.URLField(max_length = 100)
  
  def __str__(self):
    return self.platform_name

class WatchList(models.Model):
  title = models.CharField(max_length = 20)
  description = models.CharField(max_length = 200)
  platform = models.ForeignKey(StreamPlatform, on_delete = models.CASCADE, related_name = "watchlist")
  active = models.BooleanField(default = True)
  created = models.DateTimeField(auto_now_add = True)  
  
  def __str__(self):
    return self.title 
  
class Review(models.Model):
  rating = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
  watchlist = models.ForeignKey(WatchList, on_delete = models.CASCADE, related_name = "reviews")
  description = models.CharField(max_length=50, null = True)
  created = models.DateTimeField(auto_now_add = True)
  updated = models.DateTimeField(auto_now = True)
  
  def __str__(self):
    return str(self.rating) + "-" + self.watchlist.title
  
