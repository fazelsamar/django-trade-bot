from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

from utils.abstract_models import BaseModel
from utils.variables import (
    WALLET_LIST_OPTIONS,
)

from .utils.oprations import (
    subtraction_two_float,
    sum_two_float,
)

User = get_user_model()


class WalletBaseModel(BaseModel):
    """Wallet Abstract Base Model"""

    for wallet_attribute in WALLET_LIST_OPTIONS:
        vars()[wallet_attribute] = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
        """Will creates like:
        btc = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])"""

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallet")


class BlockedWallet(WalletBaseModel):
    """Will Save Total Amount Of User Blocked Money. 
       Blocked Money Can Be Used In Trade Section Or Withdraw Section.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blocked_wallet")
