from django.views.generic import DetailView
from models import Note
from haystack.views import SearchView
from utils.haystack.forms import MultiSearchForm


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'myapp/note_detail.html'


class NoteSearchView(SearchView):
    def __init__(self, *args, **kwargs):
        super(NoteSearchView, self).__init__(form_class=MultiSearchForm,
                                             *args,
                                             **kwargs)

    def build_page(self):
        (paginator, page) = super(NoteSearchView, self).build_page()

        return (paginator, page)
