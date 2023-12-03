from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now())


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Create your models here.
