from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from wallet import serializers
from wallet.models import Wallet


class WalletBalanceViewSet(ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response(serializers.WalletSerializer(instance=Wallet.get_user_wallet(user=request.user)).data)
