from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from haystack.query import SearchQuerySet


@dajaxice_register
def autocomplete(request, inputs):
    sqs = SearchQuerySet().autocomplete(content_auto=inputs)[:5]
    suggestions = [result.content_auto for result in sqs]
    data = simplejson.dumps({
        'results': suggestions
    })

    return data
