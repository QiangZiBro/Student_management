# Generated by Django 3.0.4 on 2020-03-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20200328_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='l_credit',
            field=models.FloatField(default=1, verbose_name='学分'),
        ),
    ]
