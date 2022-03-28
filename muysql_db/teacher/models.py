from django.db import models


# Create your models here.

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    main_subject = models.CharField(max_length=20)
    experience = models.IntegerField()

    def __str__(self):
        return self.teacher_name
