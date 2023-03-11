from learning_languages.languages.api.serializers import LanguageSerializer
from learning_languages.languages.models import Language
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'uuid'
