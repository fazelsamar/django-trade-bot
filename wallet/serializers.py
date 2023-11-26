from rest_framework import serializers

from utils.variables import WALLET_LIST_OPTIONS
from . import models


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wallet
        fields = [wallet_attribute for wallet_attribute in WALLET_LIST_OPTIONS] + \
                 ["blocked_" + wallet_attribute for wallet_attribute in WALLET_LIST_OPTIONS]
