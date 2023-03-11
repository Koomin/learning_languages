from learning_languages.core.api.viewsets import CoreUserViewSet
from learning_languages.languages.api.viewsets import LanguageViewSet
from learning_languages.translations.api.viewsets import TranslationViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', CoreUserViewSet, 'users')
router.register(r'languages', LanguageViewSet, 'languages')
router.register(r'translations', TranslationViewSet, 'translations')
