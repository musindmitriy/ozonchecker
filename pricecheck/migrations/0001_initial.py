# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название товара')),
                ('link', models.URLField(unique=True, verbose_name='Ссылка на товар')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата снятия цены')),
                ('price', models.PositiveIntegerField(verbose_name='Цена в рублях')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricecheck.Item')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='price',
            unique_together=set([('item', 'date')]),
        ),
    ]