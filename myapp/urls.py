from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
                       url(r'^note/(?P<pk>\d+)$',
                           NoteDetailView.as_view(),
                           name='note_detail'),
                       )
