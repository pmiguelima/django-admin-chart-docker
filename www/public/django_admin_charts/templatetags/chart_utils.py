# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.db.models import QuerySet

register = template.Library()


@register.filter(is_safe=True)
def is_iterable(value):
    return isinstance(value, (QuerySet, list, tuple))