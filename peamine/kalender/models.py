from django.db import models
from django.urls import reverse
<<<<<<< HEAD


=======
from datetime import datetime
>>>>>>> 77919efb53f4e1f0bf695554822aac863573fad4

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return '<a href="{url}"> {self.title} </a>'
