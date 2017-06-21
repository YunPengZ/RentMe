# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RentMe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent_order',
            name='store_info',
        ),
        migrations.AddField(
            model_name='rent_order',
            name='drop_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='rent_order',
            name='pick_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='rent_order',
            name='user_drive',
            field=models.CharField(max_length=12, null=True, verbose_name='驾驶证编号'),
        ),
        migrations.AlterField(
            model_name='rent_order',
            name='pick_addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pick_store', to='RentMe.store_info', verbose_name='取车门店'),
        ),
    ]
