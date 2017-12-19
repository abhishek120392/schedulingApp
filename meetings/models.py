# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Meeting(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50, null=False)
	note = models.CharField(max_length=200)
	time = models.DateTimeField(null=False)
	created_at = models.DateTimeField(null=False, auto_now=True)

	def __str__(self):
		return str(self.time) + ' : ' + self.title

	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'note': self.note,
			'time': self.time,
			'created_at': self.created_at
		}

class Invite(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	meeting = models.ForeignKey(Meeting)

	def __str__(self):
		return self.meeting.title + ' : ' + str(self.meeting.time) + ' : ' + self.user.email

	def serialize(self):
		return {
			'id': self.id,
			'user_email': self.user.email,
			'meeting_id': self.meeting_id
		}