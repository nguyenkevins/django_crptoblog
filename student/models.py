from django.db import models

# Django model "Student" stored in the database
class Student(models.Model):
    sid = models.CharField(max_length=2)
    sfname = models.CharField(max_length=15)
    slname = models.CharField(max_length=15)
    gfname = models.CharField(max_length=15)
    glname = models.CharField(max_length=15)
    semail = models.EmailField()
    scontact = models.CharField(max_length=15)
    class Meta:
        db_table = "student"