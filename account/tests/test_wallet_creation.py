from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker
import pytest

from account.models import User
from wallet.models import Wallet, BlockedWallet


@pytest.mark.django_db
class TestWalletCreation(APITestCase):
    def test_wallet_creation_for_new_user(self):
        user = baker.make(User)
        assert Wallet.objects.filter(user=user).exists()
        assert BlockedWallet.objects.filter(user=user).exists()

    def test_wallet_creation_for_new_user_in_api(self):
        username = "wallet_user_api"
        response = self.client.post(reverse('account:register'), {'username': username, 'password': '00'})
        assert response.status_code == status.HTTP_201_CREATED

        assert Wallet.objects.filter(user__username=username).exists()
        assert BlockedWallet.objects.filter(user__username=username).exists()
