from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import VerbRektion, Word, LearningSet, StateOfLearningSet, StateOfVerbRektion, StateOfWord
from .serializers import VerbRektionSerializer, LearningSetSerializer, WordSerializer


@csrf_exempt
def single_word(request):
    # get a random word
    if request.method == 'GET':
        questions = Word.objects.order_by('?').first()
        serializer = WordSerializer(questions)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def get_all_words(request):
    if request.method == 'GET':
        questions = Word.objects.all()
        serializer = WordSerializer(questions, many=True)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False}, safe=False)



def single_verb_rektion(request):
    # get a random rektion verb
    if request.method == 'GET':
        questions = VerbRektion.objects.order_by('?').first()
        serializer = VerbRektionSerializer(questions)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VerbRektionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
