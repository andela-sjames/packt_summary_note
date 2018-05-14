from django_elasticsearch_dsl import DocType, Index
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Q

client = Elasticsearch(['es:9200'])
my_search = Search(using=client)

from .models import SummaryNote

notes = Index('summarynote')

notes.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@notes.doc_type
class NotesDocument(DocType):

    class Meta:
        model = SummaryNote
        fields = ['title', 'content']

# define multi_match search 
# reference: http://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html
def elastic_search(title):
    q = Q("multi_match", query=title, fields=['title', 'content'])

    query = my_search.query(q)
    response = query.execute()

    return response
