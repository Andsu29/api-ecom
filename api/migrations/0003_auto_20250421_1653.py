# Generated by Django 3.2.25 on 2025-04-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_products_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='descricao',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='preco',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
