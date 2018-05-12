from django.db import models

# Create your models here.

class SummaryNote(models.Model):
    title = models.CharField(max_length=60)
    content = models.models.TextField()

     def __unicode__(self):
        return self.title
