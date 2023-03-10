import uuid

import pytest
from learning_languages.core.tests.factories import CoreUserFactory
from pytest_factoryboy import register


@pytest.fixture
def test_password():
    return 'password'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def api_client_authorized(db, create_user):
    from rest_framework.test import APIClient

    api_client = APIClient()
    user = create_user()
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


register(CoreUserFactory)
