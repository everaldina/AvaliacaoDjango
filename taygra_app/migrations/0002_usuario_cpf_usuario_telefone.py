# Generated by Django 5.0.6 on 2024-05-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taygra_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
