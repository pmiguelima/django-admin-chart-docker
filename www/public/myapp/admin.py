# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db.models import Count

from django_admin_charts.admin import ChartModelAdmin
from .models import MyModel, MyModelRelated


# Register your models here.

class MyModelRelatedAdmin(ChartModelAdmin, admin.ModelAdmin):
    list_display = [
        'title'
    ]
    graphics = [
        (
            'Chart - 1',
            {
                'type': 'pie',
                'axis': {
                    'created_at'
                },
                'columns': {
                }
            }
        ),
        (
            'Chart - 2',
            {
                'type': 'bar',
                'axis': {
                    'created_at'
                },
                'columns': {

                }
            }
        )
    ]


class MyModelAdmin(ChartModelAdmin, admin.ModelAdmin):
    graphics = [
        (
            'Chart - 3',
            {
                'type': 'line',
                'axis': {
                    'x': {
                        'type': 'category',
                        'categories': 'date_test'
                    }
                },
                'columns': {
                    'my_model': MyModel.objects.all().extra(select={'date_test': 'date( date_test )'}).values(
                        'date_test').annotate(total=Count('date_test'))
                }
            }
        ),
        (
            'Chart - 3',
            {
                'type': 'pie',
                'columns': {
                    'my_model': MyModel.objects.all()
                }
            }
        ),
    ]


admin.site.register(MyModelRelated, MyModelRelatedAdmin)
admin.site.register(MyModel, MyModelAdmin)
