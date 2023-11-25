from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

import pytest

User = get_user_model()


@pytest.mark.django_db
class TestRegisterUser:
    def test_if_user_creates_return_201_and_id(self):
        client = APIClient()
        response = client.post(reverse('account:register'), {'username': '1', 'password': '00'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

    def test_if_data_is_invalid_returns_400(self):
        client = APIClient()
        response1 = client.post(reverse('account:register'), {'password': '00'})
        response2 = client.post(reverse('account:register'), {'username': '1'})

        assert response1.status_code == status.HTTP_400_BAD_REQUEST
        assert response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_user_is_returns_400(self):
        client = APIClient()
        client.post(reverse('account:register'), {'username': '1', 'password': '00'})
        response = client.post(reverse('account:register'), {'username': '1', 'password': '00'})

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestTokenLoginUser:
    def test_if_user_is_authenticated_returns_200_and_token(self):
        user = User.objects.create(username='1')
        user.set_password('00')
        user.save()

        client = APIClient()
        response = client.post(reverse('account:token_login'), {'username': '1', 'password': '00'})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['token'] is not None

    def test_if_user_not_exists_returns_400(self):
        client = APIClient()
        response = client.post(reverse('account:token_login'), {'username': '1', 'password': '00'})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_username_or_password_not_match_returns_400(self):
        user = User.objects.create(username='1')
        user.set_password('00')
        user.save()

        client = APIClient()
        response1 = client.post(reverse('account:token_login'), {'username': '1', 'password': '1'})
        response2 = client.post(reverse('account:token_login'), {'username': '00', 'password': '00'})

        assert response1.status_code == status.HTTP_400_BAD_REQUEST
        assert response2.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestRegisterAndLoginUser:
    def test_if_can_log_into_registered_user_returns_id_and_token(self):
        client = APIClient()
        response1 = client.post(reverse('account:register'), {'username': '1', 'password': '00'})
        response2 = client.post(reverse('account:token_login'), {'username': '1', 'password': '00'})

        assert response1.status_code == status.HTTP_201_CREATED
        assert response1.data['id'] > 0

        assert response2.status_code == status.HTTP_200_OK
        assert response2.data['token'] is not None
