# Generated by Django 3.0.8 on 2020-08-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_noveluser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=20)),
                ('bdesc', models.CharField(max_length=250)),
                ('bauthor', models.CharField(max_length=40)),
                ('emailid', models.EmailField(max_length=254)),
            ],
        ),
    ]
