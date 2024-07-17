from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(default= 'To be written...')  
    #image = models.ImageField()
    time_to_cook = models.IntegerField(default='-1')
    instructions = models.TextField(default= 'To be written...')  

    def __str__(self):
        return self.name