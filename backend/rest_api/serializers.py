from rest_framework import serializers
from .models import VerbRektion, Word, LearningSet, StateOfLearningSet
from django.contrib.auth.models import User


class LearningSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningSet
        fields = ('id', 'title', 'type_of_set', 'date_created', 'description', 'last_success_rate')


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'learning_set', 'german_word', 'article', 'translation', 'part_of_speech')


class VerbRektionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbRektion
        fields = ('id', 'learning_set','phrase', 'case', 'translation', 'example')


class UserSerializer(serializers.ModelSerializer):
    learning_sets_states = serializers.PrimaryKeyRelatedField(many=True, queryset=StateOfLearningSet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'learning_sets_states']