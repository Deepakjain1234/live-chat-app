# Generated by Django 3.2.5 on 2021-10-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
