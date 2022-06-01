from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserBaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.user)

    class Meta:
        abstract = True