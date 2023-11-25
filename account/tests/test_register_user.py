from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

import pytest

from account.models import User


@pytest.mark.django_db
class TestTokenLoginUser(APITestCase):
    def test_if_user_is_authenticated_returns_200_and_token(self):
        user = User.objects.create(username='1')
        user.set_password('00')
        user.save()

        response = self.client.post(reverse('account:token_login'), {'username': '1', 'password': '00'})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['token'] is not None

    def test_if_user_not_exists_returns_400(self):
        response = self.client.post(reverse('account:token_login'), {'username': '1', 'password': '00'})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_username_or_password_not_match_returns_400(self):
        user = User.objects.create(username='1')
        user.set_password('00')
        user.save()

        response1 = self.client.post(reverse('account:token_login'), {'username': '1', 'password': '1'})
        response2 = self.client.post(reverse('account:token_login'), {'username': '00', 'password': '00'})

        assert response1.status_code == status.HTTP_400_BAD_REQUEST
        assert response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_can_login_into_registered_user_returns_id_and_token(self):
        response1 = self.client.post(reverse('account:register'), {'username': '1', 'password': '00'})
        response2 = self.client.post(reverse('account:token_login'), {'username': '1', 'password': '00'})

        assert response1.status_code == status.HTTP_201_CREATED
        assert response1.data['id'] > 0

        assert response2.status_code == status.HTTP_200_OK
        assert response2.data['token'] is not None
