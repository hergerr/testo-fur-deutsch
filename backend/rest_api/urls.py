from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('words', views.WordView)
router.register('verb_rektion', views.VerbsRektionView)
router.register('learning_sets', views.LearningSetView)

urlpatterns = [
    path('', include(router.urls))
]
