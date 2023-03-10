from django.db import models
from learning_languages.core.models import CoreModel


class Language(CoreModel):
    code = models.CharField(max_length=6, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    support_formality = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - ({self.code})'
