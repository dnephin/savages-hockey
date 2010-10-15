from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from hockey_register.register.models import *
from hockey_register.register.forms import AttendanceForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

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


@login_required
def update_status(request, game_id, attendance_id=None):
	" Update the users status "

	# TODO: handle missing post args or not post
	form = AttendanceForm(request.POST)
	if not form.is_valid():
		# TODO:
		return

	attendance = Attendance(player=request.user, 
			game_id=game_id, 
			state=form.cleaned_data['state'])

	# Try loading an existing status
	try:
		old_attendance = Attendance.objects.get(player=request.user, game__id=game_id)
	except ObjectDoesNotExist, e:
		pass
	else:
		old_attendance.delete()

	# TODO: error handling
	attendance.save()

	# TODO: return to proper game
	return HttpResponseRedirect(reverse('hockey_register.register.views.status'))


def status(request, game_day=None):
	" Display the attendance status for a game. "
	if game_day is None:
		today = date.today()
		days_to_friday = 4 - calendar.weekday(today.year, today.month, today.day)
		if days_to_friday < 0:
			days_to_friday = abs(days_to_friday) + 4
		game_day = (today + timedelta(days=days_to_friday)).strftime('%Y-%m-%d')


	# TODO: calculate summaries

	try:
		attendance = Attendance.objects.filter(game__game_day=game_day).order_by('player__username')
		players = User.objects.all().order_by('username')
		game = attendance[0].game if (len(attendance) > 0) else Game.objects.get(game_day=game_day)
	except ObjectDoesNotExist, e:
		return render_to_response('gamenotfound.html', {'game_date': game_day})

	attend_form = AttendanceForm()
	# TODO: set state in attendance form

	return render_to_response('status.html', RequestContext(request, 
			 {'attendances': attendance, 'players': players, 
			'game': game, 'attendance_form': attend_form}))

def add_player(request):
	" Register a new player. "
