from rest_framework import serializers
from .models import VerbRektion, VerbsRektionSet, Word, WordSet


class WordSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordSet
        fields = ('id', 'date_created', 'description', 'last_success_rate')


class VerbsRektionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbsRektionSet
        fields = ('id', 'date_created', 'description', 'last_success_rate')


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'word_set', 'german_word', 'article', 'translation', 'part_of_speech')

class VerbRektionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbRektion
        fields = ('id', 'phrase', 'case', 'translation', 'example')