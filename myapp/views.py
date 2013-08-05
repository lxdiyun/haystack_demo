from django.views.generic import DetailView
from models import Note
from haystack.views import SearchView


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'myapp/note_detail.html'


class NoteSearchView(SearchView):
    pass
