from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class TypeModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class ClothingModel(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE,related_name='clothing_items')

    def __str__(self):
        return f"{self.manufacturer} - {self.type.name} - ${self.price}"