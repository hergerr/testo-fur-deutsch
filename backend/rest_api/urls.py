from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('words/', views.get_word_and_four_answers),
]
