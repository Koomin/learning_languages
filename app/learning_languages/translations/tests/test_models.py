import pytest


@pytest.mark.django_db
def test_word_str(word_factory):
    word = word_factory()
    assert word.__str__() == f'{word.word} ({word.language.code})'


@pytest.mark.django_db
def test_translation_str(translation_factory):
    translation = translation_factory()
    assert translation.__str__() == f'{translation.original_word} - {translation.translated_word}'
