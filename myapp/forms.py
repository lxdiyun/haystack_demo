from haystack.forms import ModelSearchForm
from utils.segment import mmseg_segment


class MyAPPSearchForm(ModelSearchForm):
    def clean(self):
        cleaned_data = super(MyAPPSearchForm, self).clean()
        q = cleaned_data.get('q')
        q = mmseg_segment(q)
        cleaned_data['q'] = q

        return cleaned_data
