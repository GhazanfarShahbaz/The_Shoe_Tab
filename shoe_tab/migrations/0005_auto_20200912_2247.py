# Generated by Django 3.0.8 on 2020-09-12 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe_tab', '0004_auto_20200912_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='shoe_name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
