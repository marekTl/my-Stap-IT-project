# Generated by Django 5.0.2 on 2024-03-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervacni_system', '0012_alter_dite_akce'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dite',
            name='akce',
        ),
        migrations.AddField(
            model_name='dite',
            name='akce',
            field=models.ManyToManyField(blank=True, to='rezervacni_system.sportovniakce'),
        ),
    ]
