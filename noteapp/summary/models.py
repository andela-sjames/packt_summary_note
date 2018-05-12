from django.db import models

# Create your models here.

class SummaryNote(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()

    def __str__ (self):
        return self.title

    def __repr__ (self):
        return '<SummaryNote %s>' % self.title
