from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('myapp.views',
                       url(r'^note/(?P<pk>\d+)$',
                           NoteDetailView.as_view(),
                           name='note_detail'),
                       url(r'^search',
                           NoteSearchView(),
                           name='search_view'),
                       )
