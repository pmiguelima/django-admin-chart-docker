# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import QuerySet


class ChartModel(object):
    charts = []
    list_filter = []
    filter_class = None
    perms = []
    model = None
    display = []

    chart_template = ''
    chart_list_template = ''
    chart_list_filter_template = ''

    def get_perms(self, request):
        return self.perms

    def check_perms(self, request):
        return True

    def get_filtered_queryset(self, request, chart):
        chart[1]['columns'] = [
            (
                title,
                column.all() if isinstance(column, QuerySet) else column
            ) for title, column in self.get_columns(request, chart)
        ]
        return chart

    def get_all_charts(self, request):
        charts = []
        for chart in self.charts:
            title, settings = chart
            charts.append(
                (
                    title,
                    self.get_filtered_queryset(request, chart)[1]
                )
            )
        return charts

    def get_columns(self, request, chart):
        index = self.get_chart_index(chart)
        if index > -1:
            if hasattr(self, 'get_columns_%s' % index):
                return getattr(self, 'get_columns_%s' % index)(request)
        return chart[1]['columns']

    def get_chart_index(self, chart):
        try:
            return [x for x, y in enumerate(self.charts) if y[0] == chart[0]][0]
        except Exception:
            return -1

    def get_model(self):
        return self.model

    def get_list_filter_fields(self):
        pass

    def get_filter_class(self):
        pass

    def get_list_filter(self, request):
        return self.list_filter

    def get_preserved_filters(self, request):
        pass
