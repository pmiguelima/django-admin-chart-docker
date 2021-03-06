# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
# Register your models here.
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.text import capfirst
from .charts import ChartModel

class ChartModelAdmin(object):
    charts = None
    chart_class = None
    chartslist_view_template = 'admin/django_admin_charts/charts_list.html'

    def changelist_view(self, request, extra_context=None):
        if extra_context is not None:
            extra_context.update({
                'graphics': self.charts
            })
        else:
            extra_context = {
                'graphics': self.charts
            }
        return super(ChartModelAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_model_perms(self, request):
        perms = super(ChartModelAdmin, self).get_model_perms(request)
        if self.charts is not None or self.chart_class is not None and issubclass(self.chart_class, ChartModel):
            perms.update({
                'chart': True
            })
        return perms

    def get_urls(self):
        urls = super(ChartModelAdmin, self).get_urls()
        url_charts = [
            url('^charts/?', self.chartslist_view, name='%s_charts' % self.model._meta.model_name)
        ]
        return urls + url_charts

    def chartslist_view(self, request):
        context = {
            'opts': self.model._meta,
            'module_name': capfirst(force_text(self.model._meta.verbose_name_plural)),
            'has_permission': True,
            'charts': self.charts or self.chart_class().get_all_charts(request)
        }
        return TemplateResponse(request, self.chartslist_view_template, context=context)


admin.site.index_template = 'admin/django_admin_charts/index.html'
admin.site.app_index_template = 'admin/django_admin_charts/app_index.html'
