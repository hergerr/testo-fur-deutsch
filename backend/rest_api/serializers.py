from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class LearningSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningSet
        fields = ('id', 'title', 'type_of_set',
                  'date_created', 'description', 'last_success_rate')


class StateOfLearningSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateOfLearningSet
        fields = ('id', 'owner', 'learning_set',
                  'number_of_obligaory_rounds', 'percent_done', 'corectness_rate')


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'learning_set', 'german_word',
                  'article', 'translation', 'part_of_speech')


class StateOfWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateOfWord
        fields = ('id', 'state_of_set', 'word',
                  'done', 'number_of_correct_answers')


class VerbRektionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbRektion
        fields = ('id', 'learning_set', 'phrase', 'preposition',
                  'case', 'example', 'translation')


class StateOfVerbRektionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateOfVerbRektion
        fields = ('id', 'state_of_set', 'verb_rektion',
                  'done', 'number_of_correct_answers')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'learning_sets_states']
