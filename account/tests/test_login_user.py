from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

import pytest


@pytest.mark.django_db
class TestRegisterUser(APITestCase):
    def test_if_user_creates_return_201_and_id(self):
        response = self.client.post(reverse('account:register'), {'username': '1', 'password': '00'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

    def test_if_data_is_invalid_returns_400(self):
        response1 = self.client.post(reverse('account:register'), {'password': '00'})
        response2 = self.client.post(reverse('account:register'), {'username': '1'})

        assert response1.status_code == status.HTTP_400_BAD_REQUEST
        assert response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_user_is_duplicated_returns_400(self):
        self.client.post(reverse('account:register'), {'username': '1', 'password': '00'})
        response = self.client.post(reverse('account:register'), {'username': '1', 'password': '00'})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
