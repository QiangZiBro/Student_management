# Generated by Django 3.0.4 on 2020-03-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('l_number', models.IntegerField(primary_key=True, serialize=False)),
                ('l_name', models.CharField(max_length=30)),
                ('credit', models.CharField(max_length=6)),
                ('time', models.IntegerField()),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程管理',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sName', models.CharField(max_length=10)),
                ('sNum', models.IntegerField(max_length=15)),
                ('lName', models.CharField(max_length=10)),
                ('lNum', models.IntegerField(max_length=10)),
                ('score', models.IntegerField(max_length=3)),
                ('lCredit', models.CharField(max_length=6)),
                ('lTime', models.IntegerField(max_length=5)),
            ],
            options={
                'verbose_name': '成绩',
                'verbose_name_plural': '成绩管理',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_number', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(help_text='学生姓名', max_length=20, verbose_name='姓名')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('subject', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
                ('ID_number', models.IntegerField()),
                ('native_place', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生管理',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('t_number', models.IntegerField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=10)),
                ('t_pass', models.IntegerField(max_length=6, null=True)),
                ('t_lesson_id', models.IntegerField(max_length=10)),
                ('t_lesson_name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师管理',
            },
        ),
    ]
