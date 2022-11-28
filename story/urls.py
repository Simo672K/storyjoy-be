from django.urls import path
from . import views

urlpatterns =[
  path('', views.home, name='home-page'),
  path('story/<int:pk>/', views.story_details, name='story-details'),
  path('story/<int:pk>/<slug:slug>/', views.story_chapter, name='story-chapter'),
  path('search/', views.search, name='search')
]