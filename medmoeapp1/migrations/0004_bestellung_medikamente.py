# Generated by Django 4.2.1 on 2023-06-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medmoeapp1', '0003_alter_bestellung_bemerkung'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestellung',
            name='medikamente',
            field=models.ManyToManyField(to='medmoeapp1.medikament', verbose_name='Medikamente'),
        ),
    ]
