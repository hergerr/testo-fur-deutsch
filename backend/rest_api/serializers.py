from rest_framework import serializers
from .models import VerbRektion, Word, LearningSet, StateOfLearningSet, StateOfWord
from django.contrib.auth.models import User


class LearningSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearningSet
        fields = ('id', 'url', 'title', 'type_of_set',
                  'date_created', 'description', 'last_success_rate')


class StateOfLearningSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StateOfLearningSet
        fields = ('id', 'url', 'owner', 'learning_set',
                  'number_of_obligaory_rounds', 'percent_done', 'corectness_rate')


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'url', 'learning_set', 'german_word',
                  'article', 'translation', 'part_of_speech')


class StateOfWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StateOfWord
        fields = ('id', 'url', 'state_of_set', 'word',
                  'done', 'number_of_correct_answers')


class VerbRektionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VerbRektion
        fields = ('id', 'url', 'learning_set', 'phrase',
                  'case', 'translation', 'example')


class UserSerializer(serializers.ModelSerializer):
    learning_sets_states = serializers.PrimaryKeyRelatedField(many=True, queryset=StateOfLearningSet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'learning_sets_states']
