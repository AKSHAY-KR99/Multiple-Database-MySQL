from django.db import models


# Create your models here.

class StudentDetail(models.Model):
    name = models.CharField(max_length=25)
    course = models.CharField(max_length=15)
    year = models.CharField(max_length=10)
    marks = models.FloatField()

    def __str__(self):
        return self.name


class StudentAwards(models.Model):
    student_name = models.ForeignKey(StudentDetail, on_delete=models.CASCADE, related_name='stdent_details')
    award = models.CharField(max_length=20)

    def __str__(self):
        return str(self.student_name)
