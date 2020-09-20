import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
# "Each model has a number of class variables, each of which represents a database field
# in the model." - tutorial
# Have to assign what type each of the models fields are
# Some field 
class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)