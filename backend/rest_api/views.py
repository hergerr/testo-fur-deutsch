from django.shortcuts import render
from rest_framework import viewsets
from .models import VerbRektion, Word, LearningSet
from .serializers import VerbRektionSerializer, LearningSetSerializer, WordsSerializer


class WordView(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordsSerializer

class LearningSetView(viewsets.ModelViewSet):
    queryset = LearningSet.objects.all()
    serializer_class = LearningSetSerializer

class VerbsRektionView(viewsets.ModelViewSet):
    queryset = VerbRektion.objects.all()
    serializer_class = VerbRektionSerializer
