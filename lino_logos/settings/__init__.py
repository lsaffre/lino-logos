## Copyright 2013 Luc Saffre
## This file is part of the Lino project.
## Lino is free software; you can redistribute it and/or modify 
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## Lino is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with Lino; if not, see <http://www.gnu.org/licenses/>.

import os

from lino.projects.std.settings import *
import lino_logos
from lino_logos import SETUP_INFO as setup_info

class Site(Site):
  
    version = setup_info['version'] 
    url = setup_info['url']
    verbose_name = "Lino Logos"
    
    demo_fixtures = 'std few_languages demo demo2'.split()
    
    #~ migration_module = 'lino_logos.migrate'
    
    userdocs_prefix = 'logos.'
    
    user_model = 'users.User'
    
   
    languages = "en de fr et"
    auto_configure_logger_names = 'djangosite north lino lino_logos'
        
    def get_installed_apps(self):
        yield super(Site,self).get_installed_apps()
            
        yield 'django.contrib.contenttypes'
        yield 'django.contrib.humanize'
        yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        #~ yield 'lino.modlib.changes'
        #~ yield 'lino.modlib.countries'
        #~ yield 'lino.modlib.contacts'
        yield 'lino.modlib.languages'
        yield 'lino.modlib.comments'
        yield 'lino_logos.apps.bibles'
      

# LOGGING['logger_names'] = 'djangosite north lino lino_logos'


