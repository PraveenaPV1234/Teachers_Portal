from django.db import models
from django.contrib.auth.models import User
class Student(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Subjects_Mark(models.Model):
    student=models.ForeignKey(Student,models.CASCADE, related_name='subjects')
    subject = models.CharField(max_length=100)
    mark=models.PositiveIntegerField()
    class Meta:
        unique_together = ('student', 'subject')  # Prevents same subject for same student more than once
    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.mark}"