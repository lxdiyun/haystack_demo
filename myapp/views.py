from django.views.generic import DetailView
from models import Note
from haystack.views import SearchView
from forms import MyAPPSearchForm


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'myapp/note_detail.html'


class NoteSearchView(SearchView):
    def __init__(self, *args, **kwargs):
        super(NoteSearchView, self).__init__(form_class=MyAPPSearchForm,
                                             *args,
                                             **kwargs)
