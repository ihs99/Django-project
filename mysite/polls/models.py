import datetime

from django.db import models
from django.utils import timezone

#we’ll create two models: Question and Choice. A Question has a question and a publication date
#Here, each model is represented by a class that subclasses django.db.models.Model.
#Each model has a number of class variables, each of which represents a database field in the model.

class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text






class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



