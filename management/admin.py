# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student, Lesson, Teacher, Score, Teaching, Account


# Register your models here.
# admin.site.register(Student)


# Register your models here.
# Example
class AccountInline(admin.StackedInline):
    model = Account
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    model = Student
    # 要显示的字段
    list_display = ('s_number', 's_name', 's_gender')

    # 需要搜索的字段
    search_fields = ('s_name',)

    # 分页显示，一页的数量
    list_per_page = 10
    inlines = [AccountInline]
    actions_on_top = True


admin.site.register(Student, StudentAdmin)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('l_number', 'l_name',)

    # 需要搜索的字段
    search_fields = ('l_name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('t_number', 't_name', 't_gender')

    # 需要搜索的字段
    search_fields = ('t_name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 's_student', 's_lesson', 's_score')

    # 需要搜索的字段
    search_fields = ('s_student', 's_lesson')

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


@admin.register(Teaching)
class TeachingAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 't_teacher', 't_lesson')

    # 需要搜索的字段
    search_fields = ('t_teacher',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True
