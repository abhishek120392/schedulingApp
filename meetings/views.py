# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder

from datetime import datetime

from .models import Meeting, Invite
from utils import validateEmail


import json
# Create your views here.

def index(request):
	return HttpResponse("Welcome to meetingsApp")

def schedule_meeting(request):
	if request.method != 'POST':
		resp = {
			"status":"error", 
			"message":"Method not allowed"
		}
		return HttpResponse(json.dumps(resp, indent=2))
	req_body = request.body.decode('utf-8')
	req_body = json.loads(req_body)
	title = req_body['title']
	note = req_body['note']
	time = req_body['time']
	user_emails = req_body['user_emails']
	if len(user_emails) < 2:
		resp = {
			'status':'error', 
			'message':'Minimum 2 users in email required'
		}
		return HttpResponse(json.dumps(resp, indent=2))
	email_valid = True
	for email in user_emails:
		email_valid = email_valid and validateEmail(email)
	if email_valid == False:
		resp = {
			'status':'error', 
			'message':'invalid email ID'
		}
		return HttpResponse(json.dumps(resp, indent=2))
	for email in user_emails:
		User.objects.get_or_create(email=email, username=email)
	meeting = Meeting(title=title, note=note, time=time)
	meeting.save()
	users = User.objects.filter(email__in=user_emails)
	for user in users:
		invite = Invite(user=user, meeting=meeting)
		invite.save()
		resp = {
			'status' : 'success',
			'meeting' : meeting.serialize()
		}
	return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder, indent=2))

def get_future_meetings(request):
	if request.method != 'GET':
		resp = {
			'status':'error',
			'message':'Method not allowed'
		}
		return HttpResponse(json.dumps(resp, indent=2))
	email = request.GET.get('email')
	user = User.objects.filter(email=email)
	if user.exists():
		user = user[0]
	today = datetime.now()
	invites = Invite.objects.filter(user=user, meeting__time__gte=today)
	meetings = []
	for invite in invites:
		meetings.append(invite.meeting.serialize())
	resp = {
		'status': 'success',
		'meetings' : meetings
	}
	return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder, indent=2))