# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Student, Teacher, Lesson, Score, Account
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, "login.html")


def change(request):
    lid = int(request.GET['lid'])
    sid = int(request.GET['sid'])
    sscore = request.POST.get("score", None)
    Score.objects.filter(id=sid).update(score=sscore)
    score = Score.objects.filter(lNum=lid)
    teacher = Teacher.objects.get(t_lesson_id=lid)
    return render(request, "teacher.html", {"teacher": teacher, "score": score})


def login(request):
    mytype = request.POST.get("fruit")
    print(mytype)
    if request.method == "POST":
        mytype = request.POST.get("fruit")
        name = request.POST.get("username", None)
        ps = request.POST.get("password", None)

    if mytype == "1":

        # try:
        s = Student.objects.get(s_number=name)
        #
        # except Student.DoesNotExist:
        #     return HttpResponseRedirect("/")
        try:
            password_in_db = Account.objects.get(a_student=s).a_password
        except Exception as e:
            print(e)
        # print("id_num:{}, ps:{}".format(password_in_db, ps))
        if password_in_db == ps:
            score = Score.objects.filter(s_student=s)
            # lessons = Lesson.objects.all()
            # print(lessons)
            return render(request, "student.html", {"student": s, "score": score})
        else:
            return HttpResponseRedirect("/")
    # elif type == "2":
    #
    #     try:
    #         t = Teacher.objects.get(t_number=name)
    #     except Teacher.DoesNotExist:
    #         return HttpResponseRedirect("/")
    #     tps = t.t_pass
    #     if tps == int(ps):
    #         teacher = Teacher.objects.get(t_number=name)
    #         l_num = teacher.t_lesson_id
    #         score = Score.objects.filter(lNum=l_num)
    #         return render(request, "teacher.html", {"teacher": teacher, "score": score})
    #     else:
    #         return HttpResponseRedirect("/")
    # else:
    #     return HttpResponseRedirect("/admin/")
