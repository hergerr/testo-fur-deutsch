from rest_framework import serializers
from .models import VerbRektion, VerbsRektionSet, Word, WordSet


class WordSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordSet
        fields = ('id', 'url', 'date_created', 'description', 'last_success_rate')


class VerbsRektionSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VerbsRektionSet
        fields = ('id', 'url','date_created', 'description', 'last_success_rate')


class WordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'url','word_set', 'german_word', 'article', 'translation', 'part_of_speech')

class VerbRektionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VerbRektion
        fields = ('id', 'url','phrase', 'case', 'translation', 'example')