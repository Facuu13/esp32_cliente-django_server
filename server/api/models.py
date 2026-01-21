from django.db import models

# Create your models here.

# crear un modelo llamda DataPoint con los siguientes campos:
# source (texto), key (texto), value (decimal), ts (fecha y hora del dato), 
# created_at (fecha y hora de insercion automatica)

class DataPoint(models.Model):
    source = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=4)
    ts = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.key} : {self.value} at {self.ts}"