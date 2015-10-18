from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class GSI(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return '{}, {}'.format(str(self.user.last_name), str(self.user.first_name))


class Lab(models.Model):
    name = models.CharField(max_length=200)
    lab_date = models.DateField()

    def __str__(self):
        return str(self.name)


class Part(models.Model):
    name = models.CharField(max_length=100)
    lab = models.ForeignKey(Lab)
    is_final = models.BooleanField()

    def __str__(self):
        return "{} - {}".format(str(self.lab), str(self.name))

class Section(models.Model):
    section_id = models.IntegerField()
    lab_gsi = models.ForeignKey(GSI)

    def __str__(self):
        return "{} - {}".format(str(self.lab_gsi), str(self.section_id))


class QueueElement(models.Model):
    section = models.ForeignKey(Section)
    students = models.CommaSeparatedIntegerField(max_length=100)  # student IDs
    part = models.ForeignKey(Part)
    status = models.CharField(
        max_length=2,
        choices=(
            ('QD', 'Queued'),
            ('IP', 'In Progress'),
            ('FN', 'Finished')
        )
    )


class Student(models.Model):
    section = models.ForeignKey(Section)
    login = models.CharField(max_length=20)

    def __str__(self):
        return str(self.login)


class CompletionStatus(models.Model):
    student = models.ForeignKey(Student)
    completion = models.ForeignKey(Part)
    lab = models.ForeignKey(Lab)
