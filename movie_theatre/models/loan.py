from django.db import models

from .movie import Movie

class Loan(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    borrower = models.ForeignKey(
        'Borrower',
        on_delete=models.CASCADE
    )
    due_date = models.DateField()

    def __str__(self):
        return self.due_date