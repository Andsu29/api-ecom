# Generated by Django 3.2.25 on 2025-04-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20250421_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='categoria',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='codpro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='cor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='imagens',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='marca',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='modelo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='pid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
