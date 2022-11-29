from django.db import models
from .truck import Truck

# Create your models here.
class Patient(models.Model):
    make_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    truck = models.ForeignKey(
        # always do a hard reference here
        Truck,
        # if this author gets removed, please remove everything related to that author
        on_delete=models.CASCADE,
        # can use this to lazily refer to this later
        related_name='mechanics_of'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, mechanic of {self.docttruckor}. Last updated at: {self.updated_at}"