from django.urls import path 
from .views.movie_views import MoviesView, MovieDetailView
from .views.director_views import DirectorsView, DirectorDetailView
from .views.borrower_views import BorrowersView, BorrowerDetailView
from .views.loan_views import LoansView, LoanDetailView

urlpatterns = [
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie'),
    path('directors/', DirectorsView.as_view(), name='directors'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director'),
    path('borrowers/', BorrowersView.as_view(), name='borrowers'),
    path('borrowers/<int:pk>/', BorrowerDetailView.as_view(), name='borrower'),
    path('loans/', LoansView.as_view(), name='loans'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan'),
]