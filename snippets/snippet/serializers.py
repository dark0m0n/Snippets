from rest_framework import serializers
from snippet.models import LEXERS_CHOICES, STYLES_CHOICES
from snippet.models import Snippet


class SnippetSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titel = serializers.CharField(max_length=70)
    code = serializers.CharField()
    languege = serializers.CharField( default='python')
    style = serializers.CharField( default='igot')


    def create(self, validate_data):
        return Snippet.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.titel = validate_data.get('titel', instance.titel)
        instance.code = validate_data.get('code', instance.code)
        instance.languege = validate_data.get('languege', instance.languege)
        instance.style = validate_data.get('style', instance.style)
        instance.save()
        return instance
