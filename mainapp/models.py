from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    calories = models.IntegerField()
    protein = models.IntegerField()
    sugar = models.IntegerField()
    
    def __str__(self):
        return self.name
