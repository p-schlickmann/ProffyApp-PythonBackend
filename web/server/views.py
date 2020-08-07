from django.shortcuts import render
import time
import datetime

from server import models


# Create your views here.


def index(request):
    return render(request, "server/index.html")


def study(request):
    return render(request, "server/study.html", {
        'proffys': models.Teacher.objects.all()
    })


def teach(main_request):
    if main_request.method == 'GET':
        return render(main_request, "server/give-classes.html")
    elif main_request.method == 'POST':
        request = dict(main_request.POST)
        print(request)
        name = request.get('name')[0]
        img_url = request.get('avatar')[0]
        whatsapp = int(request.get('whatsapp')[0])
        bio = request.get('bio')[0]
        subject_id = request.get('subject')[0]
        subject_name = convert_id(subject_id)
        cost = int(request.get('cost')[0])

        week_day = request['weekday[]']
        week_day_name = [convert_id(week_day_id, day=True) for week_day_id in week_day]

        starts = request['time_from[]']
        start_seconds = [convert_to_seconds(start) for start in starts]

        ends = request.get('time_to[]')
        end_seconds = [convert_to_seconds(end) for end in ends]

        new_teacher = models.Teacher(name=name, avatar_url=img_url, whatsapp=whatsapp, bio=bio, subject=subject_id,
                                     subject_name=subject_name, cost=cost)
        new_teacher.save()

        for wk_day, wk_day_name, st, st_sec, en, end_secs in zip(week_day, week_day_name, starts, start_seconds, ends, end_seconds):
            new_class = models.Class(teacher=new_teacher, week_day=wk_day, week_day_name=wk_day_name, start=st,
                                 end=en, start_seconds=st_sec, end_seconds=end_secs)
            new_class.save()
        return render(main_request, "server/study.html", {
            'proffys': models.Teacher.objects.all()
        })


def search(request):
    subject = request.GET.get('subject', None)
    week_day = request.GET.get('weekday', None)
    time = convert_to_seconds(request.GET.get('time', None))

    matches = []
    if subject and week_day and time:
        teachers = models.Teacher.objects.filter(subject=subject)
        for teacher in teachers:
            classes = teacher.classes.filter(week_day=week_day)
            for _class in classes:
                start = _class.start_seconds
                end = _class.end_seconds - 3600
                if end >= time >= start:
                    if _class.teacher not in matches:
                        matches.append(_class.teacher)
    elif subject and week_day:
        teachers = models.Teacher.objects.filter(subject=subject)
        classes = [teacher.classes.filter(week_day=week_day) for teacher in teachers][0]
        for _class in classes:
            if _class.teacher not in matches:
                matches.append(_class.teacher)
    elif week_day and time:
        classes = models.Class.objects.filter(week_day=week_day)
        for _class in classes:
            start = _class.start_seconds
            end = _class.end_seconds - 3600
            if end >= time >= start:
                if _class.teacher not in matches:
                    matches.append(_class.teacher)
    elif subject and time:
        teachers = models.Teacher.objects.filter(subject=subject)
        for teacher in teachers:
            classes = teacher.classes.all()
            for _class in classes:
                start = _class.start_seconds
                end = _class.end_seconds - 3600
                if end >= time >= start:
                    if _class.teacher not in matches:
                        matches.append(_class.teacher)
    elif subject:
        matches = models.Teacher.objects.filter(subject=subject)
    elif week_day:
        classes = models.Class.objects.filter(week_day=week_day)
        for _class in classes:
            if _class.teacher not in matches:
                matches.append(_class.teacher)
    elif time:
        classes = models.Class.objects.all()
        for _class in classes:
            start = _class.start_seconds
            end = _class.end_seconds - 3600
            if end >= time >= start:
                if _class.teacher not in matches:
                    matches.append(_class.teacher)
    elif not week_day and not subject and not time:
        matches = models.Teacher.objects.all()
    else:
        matches = None
    return render(request, "server/study.html", {
        'proffys': matches
    })


def convert_id(_id, day=False):
    if not day:
        conv = {
            1: 'Artes',
            2: 'Biologia',
            3: 'Ciências',
            4: 'Educação Física',
            5: 'Física',
            6: 'Geografia',
            7: 'História',
            8: 'Matemática',
            9: 'Português',
            10: 'Química',
        }
    else:
        conv = {
            1: 'Domingo',
            2: 'Segunda',
            3: 'Terça',
            4: 'Quarta',
            5: 'Quinta',
            6: 'Sexta',
            7: 'Sábado',
        }

    return conv[int(_id)]


def convert_to_seconds(time):
    if not time:
        return None
    ftr = [3600, 60]

    return sum([a * b for a, b in zip(ftr, map(int, time.split(':')))])
