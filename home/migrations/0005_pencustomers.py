# Generated by Django 3.1.4 on 2021-02-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='pencustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=1, max_length=50)),
                ('upiid', models.CharField(default=1, max_length=100)),
            ],
        ),
    ]
