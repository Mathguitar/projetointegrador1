# Generated by Django 4.2 on 2023-05-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cade_meu_pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalencontrado',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='animalperdido',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]