from rest_framework import serializers

from . import models


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wallet
        fields = [
            'rial',
            'btc',
            'usdt',
            'eth',
            'blocked_rial',
            'blocked_btc',
            'blocked_usdt',
            'blocked_eth',
        ]
