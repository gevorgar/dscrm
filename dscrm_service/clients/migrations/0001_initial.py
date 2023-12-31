# Generated by Django 4.2.4 on 2023-09-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=10, verbose_name='Имя клиента')),
                ('client_phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('reklam_company', models.CharField(blank=True, max_length=20, verbose_name='Рекламная компания')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'clients',
            },
        ),
    ]
