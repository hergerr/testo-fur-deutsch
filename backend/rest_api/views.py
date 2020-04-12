import random

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *
from .serializers import *


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


@api_view(['GET', 'POST', 'PUT'])
def user_learning_set_state(request):
    permission_classes = IsOwner
    data = request.data
    data['owner'] = request.user.id

    if request.method == 'GET':
        states = StateOfLearningSet.objects.filter(owner=request.user)
        serializer = StateOfLearningSetSerializer(states, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StateOfLearningSetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        state = get_object_or_404(
            StateOfLearningSet, id=data['id'], owner=data['owner'])
        serializer = StateOfLearningSetSerializer(state, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_word_with_answer_options(request, state_of_learning_set_id):
    # tak wygląda join
    word_states = get_list_or_404(StateOfWord, state_of_set=state_of_learning_set_id, state_of_set__owner=request.user.id)
    word_state = random.choice(word_states)

    serializer = StateOfWordSerializer(word_state)
    return Response(serializer.data)
