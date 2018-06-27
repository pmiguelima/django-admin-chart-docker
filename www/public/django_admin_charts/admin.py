# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
# Register your models here.
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.text import capfirst


class ChartModelAdmin(object):
    graphics = None
    chartslist_view_template = 'admin/django_admin_charts/charts_list.html'

    def changelist_view(self, request, extra_context=None):
        if extra_context is not None:
            extra_context.update({
                'graphics': self.graphics
            })
        else:
            extra_context = {
                'graphics': self.graphics
            }
        return super(ChartModelAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_model_perms(self, request):
        perms = super(ChartModelAdmin, self).get_model_perms(request)
        if self.graphics is not None:
            perms.update({
                'chart': True
            })
        return perms

    def get_urls(self):
        urls = super(ChartModelAdmin, self).get_urls()
        info = self.model._meta.model_name
        url_charts = [
            url('^charts/?', self.chartslist_view, name='%s_charts' % info)
        ]
        return urls + url_charts

    def chartslist_view(self, request):
        context = {
            'opts': self.model._meta,
            'module_name': capfirst(force_text(self.model._meta.verbose_name_plural)),
            'has_permission': True,
            'charts': self.graphics
        }
        return TemplateResponse(request, self.chartslist_view_template, context=context)


admin.site.index_template = 'admin/django_admin_charts/index.html'
admin.site.app_index_template = 'admin/django_admin_charts/app_index.html'
