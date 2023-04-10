from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippet.models import Snippet
from snippet.serializers import SnippetSerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins

# Create your views here.
@api_view(["GET", "POST"])
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
@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(id=pk)
    except Snippet.DoesNotExist:
        return JsonResponse('!!!eror!!!', status=404, safe=False)

    if request.method == 'GET':
        serializers = SnippetSerializers(snippet)
        return JsonResponse(serializers.data, safe=False)
    if request.method == 'DELETE':
        snippet.delete()
        return JsonResponse('delete', safe=False)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = SnippetSerializers(snippet ,data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data)
        return JsonResponse(serializers.errors, status=400)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request=request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request=request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request=request, *args, **kwargs)


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request=request, *args, **kwargs)
