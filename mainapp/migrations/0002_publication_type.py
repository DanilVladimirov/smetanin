# Generated by Django 3.2.4 on 2021-06-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='type',
            field=models.CharField(choices=[('achievement', 'досягнення'), ('publication', 'публікація')], default='', max_length=100),
        ),
    ]
