from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from hockey_register.register.models import *
from hockey_register.register.forms import AttendanceForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from datetime import date, timedelta
import calendar
from collections import defaultdict


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
		old_attendance.delete()
	except ObjectDoesNotExist, e:
		pass

	# TODO: error handling
	attendance.save()

	# TODO: return to proper game
	return HttpResponseRedirect(reverse('hockey_register.register.views.status'))


def status(request, game_day=None):
	" Display the attendance status for a game. "

	# Calculate date of next Friday if not date is set
	if game_day is None:
		today = date.today()
		days_to_friday = 4 - calendar.weekday(today.year, today.month, today.day)
		if days_to_friday < 0:
			days_to_friday = 7 + days_to_friday
		game_day = (today + timedelta(days=days_to_friday)).strftime('%Y-%m-%d')

	# Retrieve data
	try:
		attendance = Attendance.objects.filter(game__game_day=game_day).order_by('player__username')
		players = User.objects.all().order_by('username')
		game = attendance[0].game if (len(attendance) > 0) else Game.objects.get(game_day=game_day)
	except ObjectDoesNotExist, e:
		return render_to_response('gamenotfound.html', {'game_date': game_day})

	# Build player hash
	player_map = dict(map(lambda p: (p.id, p), players))

	# Calculate summary
	summary = defaultdict(int)
	user_state = 'unknown'
	for attend in attendance:
		summary[attend.state] += 1
		# remove players who have responded for this game
		if attend.state != 'unknown':
			del player_map[attend.player.id]

		if attend.player.id == request.user.id:
			user_state = attend.state
	
	attend_form = AttendanceForm({'state': user_state})

	return render_to_response('status.html', RequestContext(request, 
			 {'attendances': attendance, 'players': player_map.values(), 
			'game': game, 'attendance_form': attend_form,
			'summary': summary.items()}))

def add_player(request):
	" Register a new player. "

	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('hockey_register.register.views.index'))
	else:
		form = RegisterForm()

	return render_to_response('registration/register.html', {'form': form})

