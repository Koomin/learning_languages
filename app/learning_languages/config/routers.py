from learning_languages.core.api.viewsets import CoreUserViewSet
from learning_languages.languages.api.viewsets import LanguageViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'users', CoreUserViewSet)
