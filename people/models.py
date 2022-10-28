from django.db import models

# Create your models here.
class People(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  city = models.CharField(max_length=100)

  def __str__(self):
    return self.name