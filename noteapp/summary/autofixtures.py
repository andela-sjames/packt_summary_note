from autofixture import generators, register, AutoFixture
from .models import SummaryNote

class SummaryNoteAutoFixtures(AutoFixture):
     field_values = {
        'title': generators.LoremWordGenerator(),
        'content': generators.LoremHTMLGenerator(),
    }

register(SummaryNote, SummaryNoteAutoFixtures)
