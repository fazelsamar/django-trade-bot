from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

from .utils.oprations import (
    subtraction_two_float,
    sum_two_float,
)

User = get_user_model()

class WalletBaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rial = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])

    btc = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])

    usdt = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])

    eth = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.user)

    @staticmethod
    def subtract_from_wallet_obj_by_variable_name(wallet_obj, value, variable_name):
        pre_value = wallet_obj.__getattribute__(variable_name)
        final_value = subtraction_two_float(pre_value, value)
        wallet_obj.__setattr__(variable_name, final_value)
        return wallet_obj

    @staticmethod
    def add_to_wallet_obj_by_variable_name(wallet_obj, value, variable_name):
        pre_value = wallet_obj.__getattribute__(variable_name)
        final_value = sum_two_float(pre_value, value)
        wallet_obj.__setattr__(variable_name, final_value)
        return wallet_obj

    class Meta:
        abstract = True


class Wallet(WalletBaseModel):
    """Will Save Total Amount Of User Money"""
    pass


class BlockedWallet(WalletBaseModel):
    """Will Save Total Amount Of User Blocked Money. 
       Blocked Money Can Be Used In Trade Section Or Withdraw Section.
    """
    pass