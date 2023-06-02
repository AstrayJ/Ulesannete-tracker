from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
from .models import Event
 
<<<<<<< HEAD
=======


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += '<li> {event.get_html_url} </li>'

		if day != 0:
			return "<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return '<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += '{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += '{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += '{self.formatweek(week, events)}\n'
		return cal
>>>>>>> 77919efb53f4e1f0bf695554822aac863573fad4
