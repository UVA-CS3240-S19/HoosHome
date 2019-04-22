# Generated by Django 2.1.4 on 2019-04-22 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190408_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='reviewers',
            field=models.CharField(default='[]', max_length=19000),
        ),
        migrations.AlterField(
            model_name='listing',
            name='interior_View',
            field=models.ImageField(default='static/images/rotunda', upload_to='individual', verbose_name='Interior View'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
