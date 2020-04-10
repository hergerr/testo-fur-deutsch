from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import VerbRektion, Word, LearningSet, StateOfLearningSet, StateOfVerbRektion, StateOfWord
from .serializers import VerbRektionSerializer, LearningSetSerializer, WordSerializer, UserSerializer, StateOfWordSerializer, StateOfLearningSetSerializer


class WordView(viewsets.ModelViewSet):

    queryset = Word.objects.all()
    serializer_class = WordSerializer


class StateOfWordView(viewsets.ModelViewSet):

    queryset = StateOfWord.objects.all()
    serializer_class = StateOfWordSerializer


class StateOfLearningSetView(viewsets.ModelViewSet):

    queryset = StateOfLearningSet.objects.all()
    serializer_class = StateOfLearningSetSerializer


class LearningSetView(viewsets.ModelViewSet):

    queryset = LearningSet.objects.all()
    serializer_class = LearningSetSerializer


class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


# class RegisterView(APIView):
#     def post(self, request, format=None)