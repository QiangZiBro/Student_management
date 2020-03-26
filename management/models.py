# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Student(models.Model):
    s_number = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=20,verbose_name='姓名', help_text="学生姓名")
    sex = models.CharField(max_length=2, verbose_name='性别')
    subject = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    ID_number = models.IntegerField()
    native_place = models.CharField(max_length=30)

    def __str__(self):
        return self.s_name

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生管理"


class Lesson(models.Model):
    l_number = models.IntegerField(primary_key=True)
    l_name = models.CharField(max_length=30)
    credit = models.CharField(max_length=6)
    time = models.IntegerField()

    def __str__(self):
        return self.l_name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程管理"


class Teacher(models.Model):
    t_number = models.IntegerField(primary_key=True)
    t_name = models.CharField(max_length=10)
    t_pass = models.IntegerField(max_length=6, null=True)
    t_lesson_id = models.IntegerField(max_length=10)
    t_lesson_name = models.CharField(max_length=10)

    def __str__(self):
        return self.t_name

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = "教师管理"


class Score(models.Model):
    sName = models.CharField(max_length=10)
    sNum = models.IntegerField(max_length=15)
    lName = models.CharField(max_length=10)
    lNum = models.IntegerField(max_length=10)
    score = models.IntegerField(max_length=3)
    lCredit = models.CharField(max_length=6)
    lTime = models.IntegerField(max_length=5)

    def __str__(self):
        return self.sName

    class Meta:
        verbose_name = "成绩"
        verbose_name_plural = "成绩管理"
