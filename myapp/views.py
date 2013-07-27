from django.views.generic import DetailView
from models import Note


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'myapp/note_detail.html'
