# Generated by Django 2.0.3 on 2018-03-30 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roommates_app', '0002_roommate_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
