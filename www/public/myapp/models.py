# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class MyModelRelated(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = 'My Model Related'
        verbose_name_plural = 'My Models Related'


class MyModel(models.Model):
    title = models.CharField(max_length=255)
    related = models.ForeignKey(MyModelRelated)
    description = models.TextField()
    date_test = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = 'My Model'
        verbose_name_plural = 'My Models'

