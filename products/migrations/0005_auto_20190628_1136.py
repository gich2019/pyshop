# Generated by Django 2.2.2 on 2019-06-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='FirstName',
            field=models.CharField(default='john', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='LastName',
            field=models.CharField(default='mainye', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='PhoneNumber',
            field=models.IntegerField(default=999999),
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(default='jjjj@gmail.com', max_length=70),
            preserve_default=False,
        ),
    ]
