# Generated by Django 5.0.2 on 2024-03-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervacni_system', '0005_alter_rodic_bydliste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodic',
            name='bydliste',
            field=models.CharField(max_length=80),
        ),
    ]
