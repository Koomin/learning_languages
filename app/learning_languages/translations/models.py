from django.db import models
from learning_languages.core.models import CoreModel, CoreUser
from learning_languages.languages.models import Language


class Word(CoreModel):
    word = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.word} ({self.language.code})'


class Translation(CoreModel):
    original_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='translations_original')
    translated_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='translations_translated')
    users = models.ManyToManyField(CoreUser, related_name='translations')

    def __str__(self):
        return f'{self.original_word} - {self.translated_word}'
