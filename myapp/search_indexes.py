from haystack import indexes
from myapp.models import Note
from django.utils.timezone import now
from utils.haystack.fields import ZhCharField


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = ZhCharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=now())
