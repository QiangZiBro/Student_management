# Generated by Django 3.0.4 on 2020-03-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]