# Generated by Django 4.2.7 on 2023-11-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=50)),
                ('cobertura', models.CharField(max_length=50)),
                ('recheio', models.CharField(max_length=50)),
                ('tamanho', models.CharField(max_length=10)),
                ('tipodemassa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Bolo',
                'verbose_name_plural': 'Bolos',
            },
        ),
    ]
