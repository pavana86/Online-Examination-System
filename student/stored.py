from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



# managers.py

from django.db import DatabaseError

class ExamAttemptManager(models.Manager):

    def check_number_of_attempts(self, exam, user):
        # Check if user has exceeded number of attempts for a given exam
        max_attempts = 3
        try:
            num_attempts = self.filter(exam=exam, user=user).count()
            if num_attempts >= max_attempts:
                return False
            else:
                return True
        except DatabaseError as e:
            raise e
        

class ExamAttempt(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    # Define ExamAttemptManager here
    objects = models.Manager()
    restricted_objects = ExamAttemptManager()

    def save(self, *args, **kwargs):
        if self.id is None:
            if self.restricted_objects.check_number_of_attempts(self.exam, self.user) is False:
                raise Exception("You have exceeded the maximum number of attempts for this exam.")
        super(ExamAttempt, self).save(*args, **kwargs)
