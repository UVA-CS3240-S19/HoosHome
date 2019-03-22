# Generated by Django 2.1.7 on 2019-03-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='baths',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='beds',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(),
        ),
    ]
