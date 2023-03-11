from learning_languages.core.api.serializers import CoreUserSerializer
from learning_languages.core.models import CoreUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CoreUserViewSet(viewsets.ModelViewSet):
    queryset = CoreUser.objects.all()
    serializer_class = CoreUserSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = 'uuid'
