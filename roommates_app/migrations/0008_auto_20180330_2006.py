# Generated by Django 2.0.3 on 2018-03-30 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roommates_app', '0007_auto_20180330_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaning',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roommates_app.Room'),
        ),
    ]
