# Generated by Django 4.1 on 2022-10-30 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='name',
            field=models.TextField(),
        ),
    ]