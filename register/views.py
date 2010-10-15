from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from hockey_register.register.models import Game

from datetime import date, timedelta
import calendar


def index(request):
	"""
	The index page. 
	- redirect to login page is user is not loged in.
	- redirect to next game status page if user is loged in
	"""
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))
	return HttpResponseRedirect(reverse('hockey_register.register.views.status'))


def update_status(request):
	" Update the users status "


def status(request, game_day=None):
	" Display the attendance status for a game. "
	if game_day is None:
		today = date.today()
		days_to_friday = 4 - calendar.weekday(today.year, today.month, today.day)
		if days_to_friday < 0:
			days_to_friday = abs(days_to_friday) + 4
		game_day = today + timedelta(days=days_to_friday).strftime('%Y-%m-%d')
	attendance = Attendance.objects.filter(game__game_date=game_day).orber_by('player__name')
	return render_to_response('/status.html', {'attendances': attendance})
		
