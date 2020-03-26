# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student, Lesson, Teacher, Score

# Register your models here.
# admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Score)


# Register your models here.
# Example
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('s_name', 'sex')

    # 需要搜索的字段
    search_fields = ('s_name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True
