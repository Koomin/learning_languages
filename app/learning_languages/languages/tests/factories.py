import factory
from learning_languages.languages.models import Language


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language

    code = factory.Sequence(lambda n: f'PL{n}')
    name = factory.Sequence(lambda n: f'Polish{n}')
    support_formality = factory.Faker('pybool')
