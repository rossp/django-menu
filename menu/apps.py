# -*- coding: utf-8 -*-

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _

from django.apps import AppConfig as BaseConfig


class AppConfig(BaseConfig):
    name = 'menu'
    verbose_name = _('Menu')

