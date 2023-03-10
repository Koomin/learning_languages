import uuid as uuid_lib

from django.contrib.auth.models import AbstractUser
from django.db import models


class CoreModel(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CoreUser(AbstractUser, CoreModel):
    pass
