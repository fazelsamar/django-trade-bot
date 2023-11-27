from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from model_bakery import baker
import pytest

from .conftest import get_base_wallet_response

User = get_user_model()


@pytest.mark.django_db
class TestWalletBalance(APITestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.wallet = self.user.wallet
        token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_if_no_credentials_returns_401(self):
        self.client.credentials()
        response = self.client.get(reverse('wallet:balance-list'))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_user_wallet_balance_is_zero(self):
        response = self.client.get(reverse('wallet:balance-list'))

        assert response.data == get_base_wallet_response()
        assert response.status_code == status.HTTP_200_OK

    def test_user_wallet_add_balance_response(self):
        wallet_values = get_base_wallet_response()
        for key in wallet_values.keys():
            wallet_values[key] = 1.3
            self.wallet = self.wallet.add_to_wallet_balance_by_variable_name(key, 1.3)
        self.wallet.save()
        response = self.client.get(reverse('wallet:balance-list'))

        assert response.data == wallet_values
        assert response.status_code == status.HTTP_200_OK
