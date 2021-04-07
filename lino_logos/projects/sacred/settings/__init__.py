## Copyright 2013 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)

import os

from lino.projects.std.settings import *
import lino_logos
from lino_logos import SETUP_INFO as setup_info

class Site(Site):

    version = setup_info['version']
    url = setup_info['url']
    verbose_name = "Lino Logos"

    demo_fixtures = 'std few_languages demo demo2'.split()

    userdocs_prefix = 'logos.'

    languages = "en de fr et"
    auto_configure_logger_names = 'lino lino_logos'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()

        yield 'lino.modlib.gfks'
        yield 'django.contrib.humanize'
        yield 'lino.modlib.users'
        yield 'lino.modlib.comments'
        yield 'lino_logos.lib.bibles'


    # def setup_plugins(self):
    #     """
    #     """
    #     self.plugins.comments.configure(commentable_model='bibles.Verse')
    #     super(Site, self).setup_plugins()
