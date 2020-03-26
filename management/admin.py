# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student, Lesson, Teacher, Score, Teaching, Account

# Register your models here.
# admin.site.register(Student)



@admin.register(Account)
class StudentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('a_student', 'a_password')

    # 需要搜索的字段
    search_fields = ('s_name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True

# Register your models here.
# Example
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('s_name', 's_gender')

    # 需要搜索的字段
    search_fields = ('s_name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


@admin.register(Lesson)
class StudentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('l_name',)

    # 需要搜索的字段
    search_fields = ('l_name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('t_name', 't_gender')

    # 需要搜索的字段
    search_fields = ('t_name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


@admin.register(Score)
class StudentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('s_student', 's_lesson', 's_score')

    # 需要搜索的字段
    search_fields = ('s_student', 's_lesson')

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


@admin.register(Teaching)
class StudentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('t_teacher', 't_lesson')

    # 需要搜索的字段
    search_fields = ('t_teacher',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True
