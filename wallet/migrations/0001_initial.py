# Generated by Django 4.0.4 on 2023-11-25 15:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rial', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('btc', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('usdt', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('eth', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlockedWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rial', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('btc', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('usdt', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('eth', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
