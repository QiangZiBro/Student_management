# Generated by Django 3.0.4 on 2020-03-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20200327_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='time',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='t_lesson_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='t_lesson_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='t_pass',
        ),
        migrations.AddField(
            model_name='student',
            name='s_gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=6),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='l_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]