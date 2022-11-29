from django.db import models
from .director import Director

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='directed_by'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, irected by {self.director}. Last updated at: {self.updated_at}"

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.author,
        }