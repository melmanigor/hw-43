from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
# Create your models here.

class PositionModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class WorkerModel(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    email = models.EmailField()
    position = models.ForeignKey(PositionModel, on_delete=models.CASCADE,related_name='workers')
    photo = models.ImageField(upload_to='workers_photos/', null=True, blank=True)

    def __str__(self):
        return self.name