# Generated by Django 3.2.25 on 2025-07-06 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_products_imagens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='imagens',
        ),
    ]
