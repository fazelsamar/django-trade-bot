from django.urls import path, include

from . import views

app_name = 'account'

urlpatterns = [
    path('auth-token/', views.TokenLoginView.as_view(), name='token_login'),
    path('auth-token-register/', views.Registration.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls')),
]
