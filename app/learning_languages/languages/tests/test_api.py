import pytest
from django.urls import reverse
from learning_languages.core.tests.conftest import (  # noqa
    api_client_authorized,
    create_user,
    test_password,
)
from learning_languages.languages.api.serializers import LanguageSerializer
from learning_languages.languages.models import Language


@pytest.mark.django_db
def test_languages_list(api_client_authorized, language_factory):  # noqa
    url = reverse('languages-list')
    language_factory()
    response = api_client_authorized.get(url)
    assert response.status_code == 200
    assert Language.objects.count() == len(response.data.get('results'))
    assert LanguageSerializer(Language.objects.all(), many=True).data == response.data.get('results')


@pytest.mark.django_db
def test_language_details(api_client_authorized, language_factory):  # noqa
    language = language_factory()
    url = reverse('languages-detail', args=[language.uuid])
    response = api_client_authorized.get(url)
    assert response.status_code == 200
    assert language.uuid.__str__() == response.data.get('uuid')
    assert language.name == response.data.get('name')
    assert language.code == response.data.get('code')
    assert LanguageSerializer(language).data == response.data
