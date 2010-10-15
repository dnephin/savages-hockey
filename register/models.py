from django.db import models
from django.contrib.auth.models import User

"""
 Player
 	>-<
 Game
 	--<
 Attendance

 Plater -< Attendance

"""


class Game(models.Model):

	game_date = models.DateTimeField()


class Attendance(models.model):

	STATE = (
		('yes', 'I will attent.'),
		('no', 'I wont make it.'),
		('maybe', 'I may be able to make it, I\'m not sure yet.'),
		('unknown', 'I haven\'t respodned yet.'),
	)

	game = models.ForeignKey(Game)
	player = models.ForeignKey(User)
	state = models.CharField(max_length=10, choices=STATE)

