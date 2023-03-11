from learning_languages.translations.tests.factories import (
    TranslationFactory,
    WordFactory,
)
from pytest_factoryboy import register

register(WordFactory)
register(TranslationFactory)
