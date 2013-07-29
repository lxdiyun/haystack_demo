from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utils.segment import mmseg_segment


class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={'pk': self.id})

    def get_segmented_text(self):
        return mmseg_segment(self.title) + mmseg_segment(self.body)

    def __unicode__(self):
        return self.title
