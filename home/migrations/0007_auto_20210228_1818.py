# Generated by Django 3.1.4 on 2021-02-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210228_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='pencustomers',
            name='email',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='pencustomers',
            name='mobno',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
