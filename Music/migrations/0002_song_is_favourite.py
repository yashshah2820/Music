# Generated by Django 2.2 on 2019-08-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]