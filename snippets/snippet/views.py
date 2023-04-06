from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippet.models import Snippet
from snippet.serializers import SnippetSerializers

# Create your views here.
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippet = Snippet.objects.all()
        serializers = SnippetSerializers(snippet, many=True)
        return JsonResponse(serializers.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = SnippetSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data)
        return JsonResponse(serializers.errors, status=400)
# :)
    