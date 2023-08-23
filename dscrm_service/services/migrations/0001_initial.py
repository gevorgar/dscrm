# Generated by Django 4.0 on 2023-08-23 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование услуги')),
                ('price', models.IntegerField(verbose_name='Стоимость услуги')),
                ('warranty', models.IntegerField(verbose_name='Гарантия/дней')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default='100', verbose_name='Стоимость')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Заказ', to='orders.order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Стоимость услуги',
                'verbose_name_plural': 'Стоимости услуг',
                'ordering': ['id'],
            },
        ),
    ]
