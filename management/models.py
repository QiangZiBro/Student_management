# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Student(models.Model):
    s_number = models.CharField(primary_key=True, max_length=20, verbose_name='学号（pk）')
    s_name = models.CharField(max_length=20, verbose_name='姓名', help_text="学生姓名")
    s_gender = models.CharField(default='男', verbose_name='性别', max_length=6, choices=[('male', '男'), ('female', '女')])

    ID_number = models.CharField(default="", max_length=19, null=False, verbose_name='身份证号码')
    native_place = models.CharField(default="", max_length=30, verbose_name='家庭地址')
    employ_recommend = models.TextField(verbose_name='就业推荐', max_length=30, default='CS')


    def __str__(self):
        return self.s_name

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     # some actions
    #     self.s_number = str(int(self.s_number) + 10000)
    #     return super().save(force_insert=force_insert, force_update=force_update, using=using,
    #                         update_fields=update_fields)

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生管理"


class Lesson(models.Model):
    l_number = models.AutoField(primary_key=True, verbose_name='课程号（pk）')
    l_name = models.CharField(unique=True, max_length=30, verbose_name="课程")
    l_credit = models.FloatField(default=1, verbose_name="学分")

    def __str__(self):
        return self.l_name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程管理"


class Teacher(models.Model):
    t_number = models.AutoField(primary_key=True, verbose_name='职工号（pk）')
    t_name = models.CharField(max_length=10, verbose_name="姓名")
    t_gender = models.CharField(default='男', verbose_name='性别', max_length=6, choices=[('male', '男'), ('female', '女')])

    ID_number = models.CharField(default="", max_length=19, null=False, verbose_name='身份证号码')
    native_place = models.CharField(default="", max_length=30, verbose_name='家庭地址')

    def __str__(self):
        return self.t_name

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = "教师管理"


class Teaching(models.Model):
    t_lesson = models.ForeignKey(Lesson, verbose_name="课程", default="", on_delete=models.CASCADE)
    t_teacher = models.ForeignKey(Teacher, verbose_name="任课教师", default="", on_delete=models.CASCADE)

    def __str__(self):
        return "{}({})".format(self.t_lesson, self.t_teacher)

    class Meta:
        unique_together = ("t_lesson", "t_teacher")  # 同一个老师同一门课程不能重复
        verbose_name = "教学"
        verbose_name_plural = "教学管理"


class Score(models.Model):
    s_lesson = models.ForeignKey(Lesson, verbose_name="课程", default="", on_delete=models.CASCADE)
    s_student = models.ForeignKey(Student, verbose_name="学生", default="", on_delete=models.CASCADE)
    s_score = models.IntegerField(default=0, verbose_name="分数")
    s_comment = models.TextField(default="", verbose_name="教师评语")

    def __str__(self):
        return str(self.s_score)

    class Meta:
        unique_together = ("s_student", "s_lesson")  # 同一个学生同一门课程不能重复
        verbose_name = "成绩"
        verbose_name_plural = "成绩管理"


class Account(models.Model):
    a_student = models.OneToOneField(Student, verbose_name="学生", default="", on_delete=models.CASCADE)
    a_password = models.CharField(verbose_name="密码", default="123456", max_length=20)

    class Meta:
        verbose_name = "账户"
        verbose_name_plural = "账户管理"
