# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

@python_2_unicode_compatible
class SummaryNote(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()

    def __str__ (self):
        return self.title

    def __repr__ (self):
        return '<SummaryNote %s>' % self.title
