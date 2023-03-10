# Generated by Django 4.1.5 on 2023-01-05 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos/')),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский'), ('unknown', 'Неизвестно')], max_length=10)),
                ('race', models.CharField(max_length=55)),
                ('dead', models.CharField(choices=[('dead', 'Мертвый'), ('alive', 'Живой')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('world', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('number_season', models.IntegerField()),
                ('image', models.ImageField(upload_to='photos/')),
                ('description', models.TextField()),
                ('premiere', models.DateField()),
                ('character', models.ManyToManyField(related_name='chat_to_ep', to='main.character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='birth_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birth_location', to='main.location'),
        ),
        migrations.AddField(
            model_name='character',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='main.location'),
        ),
    ]
