from django.db import models

# Create your models here.
class Quizdata(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    options={
            'db_table': 'Quizdata',
            'managed': True,
        }
class Questions(models.Model):
    name = models.CharField(max_length=200)
    options = models.CharField(max_length=255)
    correct_option = models.IntegerField()
    quiz = models.ForeignKey(Quizdata,on_delete=models.CASCADE, null=True)
    points = models.IntegerField()
    options={
            'db_table': 'Questions',
            'managed': True,
        }