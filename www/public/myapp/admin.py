# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django_admin_charts.admin import ChartModelAdmin
from .models import MyModel, MyModelRelated
from .charts import MyModelChartsModel


# Register your models here.

class MyModelRelatedAdmin(ChartModelAdmin, admin.ModelAdmin):
    list_display = [
        'title'
    ]
    charts = [
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
            'Chart - 3',
            {
                'type': 'line',
                'axis': {
                    'created_at'
                },
                'columns': {
                }
            }
        )
    ]


class MyModelAdmin(ChartModelAdmin, admin.ModelAdmin):
    chart_class = MyModelChartsModel

admin.site.register(MyModelRelated, MyModelRelatedAdmin)
admin.site.register(MyModel, MyModelAdmin)
