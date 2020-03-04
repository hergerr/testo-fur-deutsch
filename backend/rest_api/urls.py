from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('words', views.WordView)
router.register('words_sets', views.WordSetView)
router.register('verb_rektion', views.VerbsRektionView)
router.register('verb_rektion_sets', views.VerbsRektionSetView)

urlpatterns = [
    path('', include(router.urls))
]
