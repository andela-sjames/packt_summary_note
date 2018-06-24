from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q

from .models import SummaryNote
from .documents import elastic_search


# Create your views here.

class HomeView(TemplateView):
    template_name = 'all_notes.html'

    def get(self, request):
        
        query_text = request.GET.get('q', '')
        args = {}
        all_notes = SummaryNote.objects.all()

        if query_text:
            notes = self.search_note(query_text)
            args['notes'] = notes
        
        if not query_text:
            all_notes = SummaryNote.objects.all()
            args['notes'] = all_notes
        
        return render(request, self.template_name, args)

    @staticmethod
    def search_note(query_text):
        try:
            search_result = SummaryNote.objects.filter(
                Q(title__icontains=query_text) | Q(content__icontains=query_text)
            )
        except SummaryNote.DoesNotExist:
            search_result = []

        return search_result


class SearchView(TemplateView):
    template_name = 'ajax_search.html'

    def get(self, request):
        query_text = request.GET.get('q', '')
        args = {}

        search_result = elastic_search(query_text)

        if not search_result:
            search_result = []

        args['notes'] = search_result

        return render(request, self.template_name, args)
