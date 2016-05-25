# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig as BaseConfig


class AppConfig(BaseConfig):
    name = 'menu'
    verbose_name = _('Menu')
