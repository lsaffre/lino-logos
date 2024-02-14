"""
The settings.py used for building both `/docs` and `/userdocs`
"""
from ..settings import *


class Site(Site):

    title = "Lino Logos demo"

    #~ languages = 'en de fr et'
    #~ use_jasmine = True
    use_davlink = False
    use_eid_jslib = False
    remote_user_header = None  # 20121003


SITE = Site(globals())
DEBUG = True
