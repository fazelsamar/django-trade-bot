from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from utils.abstract_models import BaseModel
from utils.variables import (
    WALLET_LIST_OPTIONS,
)

from .utils.oprations import (
    subtraction_two_float,
    sum_two_float,
)
from .utils.upload_utils import upload_image_path

User = get_user_model()


class WalletTypeChoices(models.TextChoices):
    Rial = '0', _('Rial')
    BTC = '1', _('BTC')
    USDT = '2', _('USDT')
    ETH = '3', _('ETH')


class WalletStatusChoices(models.TextChoices):
    Valid = '0', _('Valid')
    Pending = '1', _('Pending')
    Failed = '2', _('Failed')


class Wallet(BaseModel):
    """Will Save Total Amount Of User Money
       Blocked Money Can Be Used In Trade Section Or Withdraw Section.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet")

    for wallet_attribute in WALLET_LIST_OPTIONS:
        vars()[wallet_attribute] = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
        """Will creates like:
        btc = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])"""

        vars()["blocked_" + wallet_attribute] = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
        """Will creates like:
        blocked_btc = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])"""

    def subtract_from_wallet_balance_by_variable_name(self, variable_name, value):
        pre_value = self.__getattribute__(variable_name)
        final_value = subtraction_two_float(pre_value, value)
        self.__setattr__(variable_name, final_value)
        return self

    def add_to_wallet_balance_by_variable_name(self, variable_name, value):
        pre_value = self.__getattribute__(variable_name)
        final_value = sum_two_float(pre_value, value)
        self.__setattr__(variable_name, final_value)
        return self

    @staticmethod
    def get_user_wallet(user):
        wallet, _ = Wallet.objects.get_or_create(user=user)
        return wallet


class InsertCrypto(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="insert_cryptos")
    wallet_type = models.CharField(max_length=1, choices=WalletTypeChoices.choices)
    mount = models.FloatField()
    transaction_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    trx_id = models.CharField(max_length=255)
    user_wallet_addr = models.CharField(max_length=255)
    admin_wallet_addr = models.CharField(max_length=255)
    user_description = models.TextField(null=True, blank=True)
    admin_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=WalletStatusChoices.choices)


class CollectCrypto(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collect_cryptos")
    wallet_type = models.CharField(max_length=1, choices=WalletTypeChoices.choices)
    mount = models.FloatField()
    fee = models.FloatField()
    trx_id = models.CharField(max_length=255, null=True, blank=True)
    user_wallet_addr = models.CharField(max_length=255)
    admin_wallet_addr = models.CharField(max_length=255, null=True, blank=True)
    user_description = models.TextField(null=True, blank=True)
    admin_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=WalletStatusChoices.choices)
