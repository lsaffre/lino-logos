"""
The settings.py used for building both `/docs` and `/userdocs`
"""
from lino_logos.settings import *

class Site(Site):
  
    title = "Lino Logos demo"
  
    #~ languages = 'en de fr et'
    #~ use_jasmine = True
    use_davlink = False
    use_extensible = False
    use_eid_jslib = False
    remote_user_header = None # 20121003
        
SITE = Site(globals())
#~ print 20130409, __file__, LOGGING
