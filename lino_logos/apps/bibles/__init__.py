## Copyright 2013-2015 Luc Saffre
## This file is part of the Lino Logos project.
## Lino Logos is free software; you can redistribute it and/or modify 
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## Lino Logos is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with Lino Logos; if not, see <http://www.gnu.org/licenses/>.

"""
The Bibles app adds models and functionality for managing Bibles
(different editions of the Bible).

"""

from lino import ad

from django.utils.translation import ugettext_lazy as _


class Plugin(ad.Plugin):
    verbose_name = _("Bibles")

    needs_plugins = ['lino.modlib.languages']

    def setup_main_menu(self, site, profile, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('bibles.Editions')
        m.add_action('bibles.Verses')
        m.add_action('bibles.SideBySideVerses')

    def setup_config_menu(self, site, profile, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('bibles.Books')

    def setup_explorer_menu(self, site, profile, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('bibles.Sections')

