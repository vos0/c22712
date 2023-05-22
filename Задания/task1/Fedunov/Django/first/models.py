from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('Название вопроса:', max_length=200)
    pub_date = models.DateTimeField('Дата публикации:')
    author = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=1)


class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Варианты ответов:', max_length=200)

class UserVariant(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    choice = models.ForeignKey(to=Choice, on_delete=models.CASCADE)