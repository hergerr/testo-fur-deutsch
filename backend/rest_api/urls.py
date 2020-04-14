from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('words', views.WordView)
router.register('words_states', views.StateOfWordView)
router.register('verb_rektion', views.VerbRektionView)
router.register('verb_rektion_states', views.StateOfVerbRektionView)
router.register('learning_sets', views.LearningSetView)
router.register('state_of_learning_sets', views.StateOfLearningSetView)

urlpatterns = [
    path('', include(router.urls)),
    path('user_learning_states/', views.user_learning_set_state),
    path('get_question/<int:state_of_learning_set_id>/', views.get_word_with_answer_options),
    path('get_verb_rektion/<int:state_of_learning_set_id>/', views.get_verb_rektion_question),
]
