from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl import DocType, Index
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch()

my_search = Search(using=client)

from .models import SummaryNote

connections.create_connection()

notes = Index('SummaryNote')

notes.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@book.doc_type
class NotesDocument(DocType):

    class Meta:
        model = SummaryNote
        fields = ['title', 'content']


# define simple search here
# Simple search function
def elastic_search(title):
    query = my_search.query("match", title=title)
    response = query.execute()
    return response
