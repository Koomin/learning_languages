import pytest
from django.urls import reverse
from learning_languages.core.api.serializers import CoreUserSerializer
from learning_languages.core.models import CoreUser


@pytest.mark.django_db
def test_users_list(api_client_authorized):
    url = reverse('users-list')
    response = api_client_authorized.get(url)
    assert response.status_code == 200
    assert len(response.data.get('results')) == CoreUser.objects.count()
    assert response.data.get('results') == CoreUserSerializer(CoreUser.objects.all(), many=True).data


@pytest.mark.django_db
def test_user_details(api_client_authorized, create_user):
    user = create_user()
    url = reverse('users-detail', args=[user.uuid])
    response = api_client_authorized.get(url)
    assert response.status_code == 200
    assert user.username == response.data.get('username')
    assert user.uuid.__str__() == response.data.get('uuid')
    assert CoreUserSerializer(user).data == response.data
