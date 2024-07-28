from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Student/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
    
from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    max_attempts = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class ExamAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    attempt_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'exam',)

from django.core.exceptions import PermissionDenied

class ExamAttemptManager(models.Manager):
    def create(self, student, exam):
        if ExamAttempt.objects.filter(student=student, exam=exam).exists():
            raise PermissionDenied('You have already attempted this exam.')
        return super().create(student=student, exam=exam)
    
class ExamAttempt(models.Model):
    # ...
    objects = ExamAttemptManager()