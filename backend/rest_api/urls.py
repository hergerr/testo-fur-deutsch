from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('words/', views.single_word),
    path('all_words/', views.get_all_words)
]
