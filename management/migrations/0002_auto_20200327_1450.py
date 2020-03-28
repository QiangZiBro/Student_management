# Generated by Django 3.0.4 on 2020-03-27 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='a_student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management.Student', unique=True, verbose_name='学生'),
        ),
        migrations.AlterField(
            model_name='score',
            name='s_lesson',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management.Teaching', verbose_name='课程'),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('s_student', 's_lesson')},
        ),
    ]
