# Generated by Django 4.0.5 on 2022-06-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('about', models.CharField(max_length=100, null=True, verbose_name='About')),
                ('debuts', models.CharField(max_length=50, null=True, verbose_name='Debuts')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]