# Generated by Django 5.1.7 on 2025-03-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_produto_desenvolvedor_produto_distribuidor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='desenvolvedor',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
