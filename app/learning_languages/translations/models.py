from django.db import models
from learning_languages.core.models import CoreModel
from learning_languages.languages.models import Language


class Word(CoreModel):
    word = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class Translation(CoreModel):
    original_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='translations_original')
    translated_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='translations_translated')
