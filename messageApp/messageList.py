"""
 There should be a insightful documentation here
"""

class MessageList():
	def __init__(self, messages):
		self.strings = messages
		# Convert keys to units
		withUnits = [ (self._timeToUnits(time), text) for time, text in messages ]
		self.messages = list(reversed(sorted(withUnits)))

	def getMessage(self, unit):
		for (time, message) in self.messages:
			if time <= unit:
				return message
		return None

	def _timeToUnits(self, time):
		hours = int(time[0:2])
		minutes = int(time[3:5])
		units = (hours * 60) + minutes
		return units

	def __str__(self):
		txt = ''
		for hours, message in self.strings:
			txt = txt + "\n" + hours + " " + message
		return txt
