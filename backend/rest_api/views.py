from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import VerbRektion, Word, LearningSet, StateOfLearningSet, StateOfVerbRektion, StateOfWord
from .serializers import VerbRektionSerializer, LearningSetSerializer, WordSerializer, UserSerializer, StateOfWordSerializer, StateOfLearningSetSerializer
from .permissions import IsOwner


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
        state = get_object_or_404(StateOfLearningSet, id=data['id'], owner=data['owner'])
        print(state.corectness_rate)
        print(data)
        serializer = StateOfLearningSetSerializer(state, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
