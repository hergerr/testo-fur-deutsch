from rest_framework import serializers
from .models import VerbRektion, Word, LearningSet


class LearningSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearningSet
        fields = ('id', 'url', 'title', 'type_of_set', 'date_created', 'description', 'last_success_rate')


class WordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'url', 'learning_set', 'german_word', 'article', 'translation', 'part_of_speech')

class VerbRektionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VerbRektion
        fields = ('id', 'url','learning_set','phrase', 'case', 'translation', 'example')