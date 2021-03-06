# Generated by Django 2.0.2 on 2019-05-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('languages', models.CharField(max_length=200)),
                ('github_link', models.CharField(max_length=500)),
            ],
        ),
    ]
