import factory
from learning_languages.languages.tests.factories import LanguageFactory
from learning_languages.translations.models import Translation, Word


class WordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Word

    word = factory.Sequence(lambda n: f'TestWord{n}')
    language = factory.SubFactory(LanguageFactory)


class TranslationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Translation

    original_word = factory.SubFactory(WordFactory)
    translated_word = factory.SubFactory(WordFactory)
