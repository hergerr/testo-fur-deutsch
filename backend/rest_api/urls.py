from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('words', views.WordView)
router.register('learning_sets', views.LearningSetView)
router.register('users', views.UserView)
router.register('words_states', views.StateOfWordView)
router.register('state_of_learning_set', views.StateOfLearningSetView)

urlpatterns = [
    path('', include(router.urls)),
    path('get_my_views/', views.user_learning_set_state)
]
