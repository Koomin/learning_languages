from learning_languages.translations.api.serializers import (
    TranslationSerializer,
    WordSerializer,
)
from learning_languages.translations.models import Translation, Word
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'uuid'


class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'uuid'
