# Generated by Django 5.0.4 on 2024-04-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_alumni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realalumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobileno', models.IntegerField()),
                ('password', models.CharField(max_length=14)),
            ],
        ),
    ]
