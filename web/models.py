from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_id = models.IntegerField()
    level = models.ForeignKey(Level)

    def __str__(self):
        return self.first_name
