# Generated by Django 5.0.2 on 2024-03-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervacni_system', '0004_alter_rodic_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodic',
            name='bydliste',
            field=models.CharField(max_length=100),
        ),
    ]
