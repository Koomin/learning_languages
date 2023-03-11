import factory
from learning_languages.core.models import CoreUser


class CoreUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CoreUser

    username = factory.Sequence(lambda n: f'TestUser{n}')
    first_name = factory.Sequence(lambda n: f'TestFirstName{n}')
    last_name = factory.Sequence(lambda n: f'TestLastName{n}')
    email = factory.Sequence(lambda n: f'testmail{n}@mail.com')
