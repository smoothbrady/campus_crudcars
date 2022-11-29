from django.db import models

from .movie import Movie
from .loan import Loan

class Borrower(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    borrowed_movies = models.ManyToManyField(
        Movie,
        through=Loan,
        through_fields=('borrower', 'movie')
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"