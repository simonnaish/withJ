from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class CourseType(models.Model):
    name = models.CharField(max_length=32)
    shortcut = models.CharField(max_length=2)
    max_amount_of_people = models.PositiveIntegerField()


class Specialization(models.Model):
    name=models.CharField(max_length=32)


class Instructor(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    skills = models.ManyToManyField(Specialization)


class Client(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Course(models.Model):
    course_type = models.ForeignKey(CourseType, on_delete=models.PROTECT)
    date_time = models.DateTimeField()
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.SET_NULL)
    clients = models.ManyToManyField(Client, through='ClientCourses')

class ClientCourses(models.Model):
    client=models.ForeignKey(Client, on_delete=models.PROTECT)
    course=models.ForeignKey(Course, on_delete=models.PROTECT)

    course_duration=models.DurationField(default=0)