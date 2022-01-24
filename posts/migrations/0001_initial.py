# Generated by Django 4.0.1 on 2022-01-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('dt_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
            ],
        ),
    ]