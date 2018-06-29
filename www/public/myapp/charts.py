# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count

from django_admin_charts.charts import ChartModel
from .models import MyModel


class MyModelChartsModel(ChartModel):
    model = MyModel
    list_filter = [
        'date_test'
    ]
    queryset = model.objects.extra(select={'date_test': 'date( date_test )'}).values('date_test').annotate(
        total=Count('date_test'))
    charts = [
        (
            'Chart - 2',
            {
                'type': 'line',
                'axis': {
                    'x': {
                        'type': 'category',
                        'categories': 'date_test'
                    }
                },
                'columns': {
                },
            }
        ),
        (
            'Chart - 3',
            {
                'type': 'bar',
                'axis': {
                    'x': {
                        'type': 'category',
                        'categories': 'date_test'
                    }
                },
                'groups': [
                    [
                        'Teste1',
                        'Teste2',
                    ]
                ],
                'columns': {
                    ('Teste1', queryset.filter(related__pk=1)),
                    ('Teste2', queryset.filter(related__pk=2)),
                },
                'colors': [
                    'FF3ABD',
                    'E375E8',
                    'CC46FF',
                    '8E34E8',
                    '6F3AFF'
                ]
            }
        ),
        (
            'Chart - 4',
            {
                'type': 'pie',
                'columns': {
                },
            }
        ),
        (
            'Chart - 5',
            {
                'type': 'pie',
                'columns': {
                },
            }
        )
    ]

    def get_columns_0(self, request):
        queryset = self.model.objects.values('related__pk', 'related__title').annotate(
            total=Count('related__title')).all()
        columns = []
        for column in queryset:
            data = []
            for cat in self.queryset.all():
                result = self.queryset.filter(related__pk=column['related__pk']).filter(
                    date_test__date=cat['date_test'])
                data.append(
                    result[0] if len(result) > 0 else 0
                )
            columns.append(
                (
                    column['related__title'],
                    data
                )
            )
        return columns

    def get_columns_2(self, request):
        queryset = self.queryset
        columns = []
        for column in queryset:
            columns.append(
                (
                    column['date_test'],
                    column['total']
                )
            )
        return columns

    def get_columns_3(self, request):
        queryset = self.model.objects.values('related__title').annotate(total=Count('related__title'))
        columns = []
        for column in queryset:
            columns.append(
                (
                    column['related__title'],
                    column['total']
                )
            )
        return columns
