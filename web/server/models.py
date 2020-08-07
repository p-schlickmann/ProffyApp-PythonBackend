from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=64)
    avatar_url = models.CharField(max_length=2048)
    whatsapp = models.IntegerField()
    bio = models.CharField(max_length=500)
    subject = models.IntegerField()
    subject_name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.subject_name}: {self.name} | {self.cost}R$"


class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')
    week_day = models.IntegerField()
    week_day_name = models.CharField(max_length=20)
    start = models.CharField(max_length=5)
    end = models.CharField(max_length=5)
    start_seconds = models.IntegerField()
    end_seconds = models.IntegerField()

    def __str__(self):
        return f"{self.teacher} | from {self.start} to {self.end}, {self.week_day_name}"

