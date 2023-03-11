import pytest
from django.urls import reverse
from learning_languages.core.tests.conftest import (  # noqa
    api_client_authorized,
    create_user,
    test_password,
)
from learning_languages.core.tests.factories import CoreUserFactory
from learning_languages.translations.api.serializers import (
    TranslationSerializer,
    WordSerializer,
)
from learning_languages.translations.models import Translation, Word


@pytest.mark.django_db
def test_translations_list(api_client_authorized, translation_factory):  # noqa
    url = reverse('translations-list')
    translation_factory()
    response = api_client_authorized.get(url)
    assert response.status_code == 200
    assert Translation.objects.count() == len(response.data.get('results'))
    assert TranslationSerializer(Translation.objects.all(), many=True).data == response.data.get('results')


@pytest.mark.django_db
def test_translation_details(api_client_authorized, translation_factory):  # noqa
    translation = translation_factory(users=[CoreUserFactory() for _ in range(3)])
    url = reverse('translations-detail', args=[translation.uuid])
    response = api_client_authorized.get(url)
    assert response.status_code == 200
    assert translation.uuid.__str__() == response.data.get('uuid')
    assert translation.original_word.uuid == response.data.get('original_word')
    assert translation.original_word.word == response.data.get('original_word_str')
    assert translation.original_word.language.uuid.__str__() == response.data.get('original_word_language')
    assert translation.original_word.language.name == response.data.get('original_word_language_name')
    assert translation.translated_word.uuid == response.data.get('translated_word')
    assert translation.translated_word.word == response.data.get('translated_word_str')
    assert translation.translated_word.language.uuid.__str__() == response.data.get('translated_word_language')
    assert translation.translated_word.language.name == response.data.get('translated_word_language_name')
    assert TranslationSerializer(translation).data == response.data
    assert list(translation.users.values_list('uuid', flat=True)) == response.data.get('users')


@pytest.mark.django_db
def test_words_list(api_client_authorized, word_factory):  # noqa
    url = reverse('words-list')
    word_factory()
    response = api_client_authorized.get(url)
    assert response.status_code == 200
    assert Word.objects.count() == len(response.data.get('results'))
    assert WordSerializer(Word.objects.all(), many=True).data == response.data.get('results')


@pytest.mark.django_db
def test_word_details(api_client_authorized, word_factory):  # noqa
    word = word_factory()
    url = reverse('words-detail', args=[word.uuid])
    response = api_client_authorized.get(url)
    assert response.status_code == 200
    assert word.uuid.__str__() == response.data.get('uuid')
    assert word.word == response.data.get('word')
    assert word.language.uuid == response.data.get('language')
    assert word.language.name == response.data.get('language_name')
    assert word.language.code == response.data.get('language_code')
