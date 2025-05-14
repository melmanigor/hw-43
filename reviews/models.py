from django.db import models
from clothing.models import ClothingModel

class ReviewModel(models.Model):
    clothing = models.ForeignKey(ClothingModel, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    def __str__(self):
        return f"{self.rating} - {self.comment}"
