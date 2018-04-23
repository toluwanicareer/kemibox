# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class KemiBox(models.Model):
	'''
	This  model will help you categorise your post under one box called kemibox
	'''
	user=models.ForeignKey(User)
	name=models.CharField(max_length=200)
	hashtags=models.TextField()
	
	status=models.CharField(max_length=50, choices=(('On', 'On'), ('Off', 'Off')))
	KemiBox_type=models.CharField(max_length=100, choices=(('Regular', 'Regular'), ('Once And Done','Once And Done' ), ('Date Range', 'Date Range')))






class Post(models.Model):
	content=models.TextField()
	thumbnail=models.ImageField(upload_to='media', null=True)
	last_posted=models.DateTimeField(null=True)
	kemibox=models.ForeignKey(KemiBox)
	user=models.ForeignKey(User)









