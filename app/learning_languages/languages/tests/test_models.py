import pytest


@pytest.mark.django_db
def test_language_str(language_factory):
    language = language_factory()
    assert language.__str__() == f'{language.name} - ({language.code})'
