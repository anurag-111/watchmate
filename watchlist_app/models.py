from django.db import models

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
  active = models.BooleanField(default = True)
  created = models.DateTimeField(auto_now_add = True)  
  
  def __str__(self):
    return self.title  