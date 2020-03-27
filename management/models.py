# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Student(models.Model):
    s_number = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=20, verbose_name='姓名', help_text="学生姓名")
    s_gender = models.CharField(default='男', verbose_name='性别', max_length=6, choices=[('male', '男'), ('female', '女')])

    ID_number = models.IntegerField(null=False, verbose_name='身份证号码')
    native_place = models.CharField(max_length=30,verbose_name='家庭地址')

    def __str__(self):
        return self.s_name

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生管理"


class Lesson(models.Model):
    l_number = models.AutoField(primary_key=True)
    l_name = models.CharField(unique=True, max_length=30, verbose_name="课程")

    def __str__(self):
        return self.l_name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程管理"


class Teacher(models.Model):
    t_number = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=10, verbose_name="姓名")
    t_gender = models.CharField(default='男', verbose_name='性别', max_length=6, choices=[('male', '男'), ('female', '女')])

    def __str__(self):
        return self.t_name

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = "教师管理"


class Score(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_lesson = models.ForeignKey(Lesson, verbose_name="课程", default="", on_delete=models.CASCADE)
    s_student = models.ForeignKey(Student, verbose_name="学生", default="", on_delete=models.CASCADE)
    s_score = models.IntegerField(default=0, verbose_name="分数")

    def __str__(self):
        return str(self.s_score)

    class Meta:
        verbose_name = "成绩"
        verbose_name_plural = "成绩管理"


class Teaching(models.Model):
    t_lesson = models.ForeignKey(Lesson, verbose_name="课程", default="", on_delete=models.CASCADE)
    t_teacher = models.ForeignKey(Teacher, verbose_name="任课教师", default="", on_delete=models.CASCADE, unique=True)

    class Meta:
        verbose_name = "教学"
        verbose_name_plural = "教学管理"


class Account(models.Model):
    a_student = models.ForeignKey(Student, verbose_name="学生", default="", on_delete=models.CASCADE)
    a_password = models.CharField(verbose_name="密码", default="123456", max_length=20)

    class Meta:
        verbose_name = "账户"
        verbose_name_plural = "账户管理"
