# Generated by Django 4.2.1 on 2023-06-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medmoeapp1', '0003_alter_ueberweisung_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='termin',
            name='erledigt',
            field=models.BooleanField(default=False, verbose_name='Erledigt'),
        ),
    ]
