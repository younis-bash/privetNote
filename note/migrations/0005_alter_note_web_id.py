# Generated by Django 3.2.7 on 2022-05-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20220512_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='web_id',
            field=models.CharField(max_length=200),
        ),
    ]
