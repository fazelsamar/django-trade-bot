from django.db.models.signals import post_save
from django.dispatch import receiver

from wallet.models import Wallet, BlockedWallet
from .models import User


@receiver(post_save, sender=User)
def create_wallet_for_user(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
        BlockedWallet.objects.create(user=instance)
