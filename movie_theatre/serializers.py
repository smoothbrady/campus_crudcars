from rest_framework import serializers

from .models.movie import Movie
from .models.director import Director
from .models.borrower import Borrower
from .models.loan import Loan

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movie

class MovieReadSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Movie

class DirectorSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Director

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Borrower

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Loan

class LoanReadSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    borrower = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Loan