# Generated by Django 3.2.4 on 2021-10-16 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('dis', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'newtable',
            },
        ),
    ]
