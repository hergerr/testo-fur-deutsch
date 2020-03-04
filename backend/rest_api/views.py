from django.shortcuts import render
from rest_framework import viewsets
from .models import VerbRektion, VerbsRektionSet, Word, WordSet
from .serializers import VerbRektionSerializer, VerbsRektionSetSerializer, WordSetSerializer, WordsSerializer


class WordView(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordsSerializer

class WordSetView(viewsets.ModelViewSet):
    queryset = WordSet.objects.all()
    serializer_class = WordSetSerializer

class VerbsRektionView(viewsets.ModelViewSet):
    queryset = VerbRektion.objects.all()
    serializer_class = VerbRektionSerializer

class VerbsRektionSetView(viewsets.ModelViewSet):
    queryset = VerbsRektionSet.objects.all()
    serializer_class = WordSetSerializer