# Generated by Django 4.2.1 on 2023-06-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('zeile1', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='1. Adresszeile (Name)')),
                ('zeile2', models.CharField(max_length=50, verbose_name='2. Adresszeile (Straße)')),
                ('zeile3', models.CharField(max_length=50, verbose_name='3. Adresszeile (PLZ Ort)')),
                ('zeile4', models.CharField(blank=True, max_length=50, verbose_name='4. Adresszeile')),
                ('zeile5', models.CharField(blank=True, max_length=50, verbose_name='5. Adresszeile')),
                ('zeile6', models.CharField(blank=True, max_length=50, verbose_name='6. Adresszeile')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='E-Mail')),
                ('telefon', models.CharField(blank=True, max_length=50, verbose_name='E-Telefon')),
            ],
            options={
                'verbose_name': 'Kontakt',
                'verbose_name_plural': 'Kontakts',
            },
        ),
        migrations.CreateModel(
            name='Medikament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=50, verbose_name='Bezeichnung')),
                ('details', models.CharField(max_length=100, verbose_name='Details')),
                ('menge', models.IntegerField(verbose_name='Menge in Packung')),
                ('einnahme', models.IntegerField(verbose_name='Regelmäßige Einnahme (Tag)')),
                ('letze_bestellung', models.DateField(auto_now_add=True, verbose_name='Letzte Bestellung')),
                ('letzte_lieferung', models.DateField(blank=True, verbose_name='Letzte Lieferung')),
            ],
            options={
                'verbose_name': 'Medikament',
                'verbose_name_plural': 'Medikamente',
            },
        ),
    ]
