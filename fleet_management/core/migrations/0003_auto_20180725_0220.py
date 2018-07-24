# Generated by Django 2.0.6 on 2018-07-24 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
