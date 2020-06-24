import random

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Q
from .models import *
from .serializers import *


class WordView(viewsets.ModelViewSet):

    queryset = Word.objects.all()
    serializer_class = WordSerializer


class StateOfWordView(viewsets.ModelViewSet):

    queryset = StateOfWord.objects.all()
    serializer_class = StateOfWordSerializer


class VerbRektionView(viewsets.ModelViewSet):

    queryset = VerbRektion.objects.all()
    serializer_class = VerbRektionSerializer

class StateOfVerbRektionView(viewsets.ModelViewSet):

    queryset = StateOfVerbRektion.objects.all()
    serializer_class = StateOfVerbRektionSerializer


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
    word_states = get_list_or_404(StateOfWord, done=False, state_of_set=state_of_learning_set_id, state_of_set__owner=request.user.id)
    word_state = random.choice(word_states)

    correct_word = word_state.word

    part_of_speech = correct_word.part_of_speech

    # excludowanie wybranego slowka
    possible_answers = get_list_or_404(Word, ~Q(id = correct_word.id), part_of_speech=part_of_speech)
    answers = random.sample(possible_answers, k=3)
    answer_attributes = [a.translation for a in answers]

    final_dict = {
        "word_state_id": word_state.id,
        "correct_answers": word_state.number_of_correct_answers,
        "question": correct_word.german_word,
        "corrent_answer": correct_word.translation,
        "wrong_answers": answer_attributes,
    }

    if correct_word.article:
        final_dict['article'] = correct_word.article

    return Response(final_dict, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_verb_rektion_question(request, state_of_learning_set_id):
    verb_rektion_states = get_list_or_404(StateOfVerbRektion, done=False, state_of_set=state_of_learning_set_id, state_of_set__owner=request.user.id)
    verb_rektion_state = random.choice(verb_rektion_states)

    verb_rektion = verb_rektion_state.verb_rektion

    final_dict = {
        "verb_rection_state_id": verb_rektion_state.id,
        "correct_answers": verb_rektion_state.number_of_correct_answers,
        "phrase": verb_rektion.phrase,
        "case": verb_rektion.case,
        "translation": verb_rektion.translation,
        "example": verb_rektion.example
    }

    return Response(final_dict, status=status.HTTP_200_OK)
