# Generated by Django 3.2.7 on 2022-05-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_auto_20220515_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]