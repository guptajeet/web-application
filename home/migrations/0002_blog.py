# Generated by Django 3.0.8 on 2020-07-29 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
