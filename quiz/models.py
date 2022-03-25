from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.

class user_detail(models.Model):
	username=models.CharField(max_length=150)
	no_of_test=models.IntegerField()
	total_score=models.IntegerField()
	t1=models.IntegerField()
	t2=models.IntegerField()
	t3=models.IntegerField()
	def __str__(self):
		return self.username

class question_database(models.Model):
	question_text=models.CharField(max_length=500)
	choice1=models.CharField(max_length=200)
	choice2=models.CharField(max_length=200)
	choice3=models.CharField(max_length=200)
	choice4=models.CharField(max_length=200)
	answer=models.IntegerField()
	question_type=models.CharField(max_length=200,null=True,blank=True)
	def __str__(self):
		return self.question_text

class temparory(models.Model):
	question_text=models.CharField(max_length=500)
	choice1=models.CharField(max_length=200)
	choice2=models.CharField(max_length=200)
	choice3=models.CharField(max_length=200)
	choice4=models.CharField(max_length=200)
	answer=models.IntegerField()
	def __str__(self):
		return self.question_text

class question_java(models.Model):
	question_text=models.CharField(max_length=500)
	choice1=models.CharField(max_length=200)
	choice2=models.CharField(max_length=200)
	choice3=models.CharField(max_length=200)
	choice4=models.CharField(max_length=200)
	answer=models.IntegerField()
	def __str__(self):
		return self.question_text

class question_algorithm(models.Model):
	question_text=models.CharField(max_length=500)
	choice1=models.CharField(max_length=200)
	choice2=models.CharField(max_length=200)
	choice3=models.CharField(max_length=200)
	choice4=models.CharField(max_length=200)
	answer=models.IntegerField()
	def __str__(self):
		return self.question_text

class question_python(models.Model):
	question_text=models.CharField(max_length=500)
	choice1=models.CharField(max_length=200)
	choice2=models.CharField(max_length=200)
	choice3=models.CharField(max_length=200)
	choice4=models.CharField(max_length=200)
	answer=models.IntegerField()
	def __str__(self):
		return self.question_text