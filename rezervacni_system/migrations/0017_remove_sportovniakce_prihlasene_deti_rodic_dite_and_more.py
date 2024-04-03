# Generated by Django 5.0.2 on 2024-03-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervacni_system', '0016_remove_rodic_poznamka_dite_poznamka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportovniakce',
            name='prihlasene_deti',
        ),
        migrations.AddField(
            model_name='rodic',
            name='dite',
            field=models.ManyToManyField(related_name='prirad_rodice', to='rezervacni_system.dite'),
        ),
        migrations.AlterField(
            model_name='dite',
            name='rodice',
            field=models.ManyToManyField(related_name='prirad_dite', to='rezervacni_system.rodic'),
        ),
    ]
