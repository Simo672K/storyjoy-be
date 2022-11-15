from django.urls import path
from . import views

urlpatterns =[
  path('', views.home),
  path('story/<int:pk>/', views.story_details, name='story-details'),
]