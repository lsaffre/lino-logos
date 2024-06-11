## Copyright 2013-2015 Luc Saffre
"""
The Bibles app adds models and functionality for managing Bibles
(different editions of the Bible).

.. autosummary::
   :toctree:

   models
   loader


"""

from lino import ad

from django.utils.translation import gettext_lazy as _


class Plugin(ad.Plugin):
    verbose_name = _("Bibles")

    needs_plugins = ['lino.modlib.languages']

    def setup_main_menu(self, site, profile, m, ar=None):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('bibles.Editions')
        m.add_action('bibles.Verses')
        m.add_action('bibles.SideBySideVerses')

    def setup_config_menu(self, site, profile, m, ar=None):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('bibles.Books')

    def setup_explorer_menu(self, site, profile, m, ar=None):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('bibles.Sections')
