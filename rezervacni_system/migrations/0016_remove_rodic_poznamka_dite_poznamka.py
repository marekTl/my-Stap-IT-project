# Generated by Django 5.0.2 on 2024-03-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervacni_system', '0015_sportovniakce_prihlasene_deti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rodic',
            name='poznamka',
        ),
        migrations.AddField(
            model_name='dite',
            name='poznamka',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
