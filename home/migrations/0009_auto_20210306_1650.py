# Generated by Django 3.1.4 on 2021-03-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210305_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='resum',
            name='icourse',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='resum',
            name='scourse',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
