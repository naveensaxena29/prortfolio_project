from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),

    # Project case study
    path('projects/food/', views.food_project, name='food_project'),
    path('projects/book-review/', views.book_review, name='book_review'),
    path('projects/cake-customize/', views.cake_customize, name='cake_customize'),

    
]


