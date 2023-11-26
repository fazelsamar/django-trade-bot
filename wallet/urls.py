from rest_framework import routers

from . import views

app_name = "wallet"

router = routers.DefaultRouter()
router.register('balance', views.WalletBalanceViewSet, basename='balance')

urlpatterns = router.urls
