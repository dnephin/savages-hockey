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

	game_day = models.DateField(unique=True, db_index=True)
	game_time = models.TimeField()


	def __str__(self):
		return "Game at %s %s" % (self.game_day, self.game_time)


class Attendance(models.Model):


	class Meta:
		unique_together = ('game', 'player')

	STATE = (
		('yes', 'I\'ll be there.'),
		('no', 'I wont make it.'),
		('maybe', 'I may be able to make it, I\'m not sure yet.'),
		('unknown', 'I haven\'t respodned yet.'),
	)

	game = models.ForeignKey(Game)
	player = models.ForeignKey(User)
	state = models.CharField(max_length=10, choices=STATE)

	def __str__(self):
		return "Attendance for %s at game %s: %s" % (self.player, self.game, self.state)

