from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, made by {self.company}. Last updated at: {self.updated_at}"

    def as_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'company': self.company,
        }