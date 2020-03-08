from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import VerbRektion, Word, LearningSet, StateOfLearningSet, StateOfVerbRektion, StateOfWord
from .serializers import VerbRektionSerializer, LearningSetSerializer, WordsSerializer


@csrf_exempt
def get_word_and_four_answers(request):
    if request.method == 'GET':
        questions = Word.objects.all()
        serializer = WordsSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)