from lino_logos.settings.demo import *
SITE = Site(globals(),title = "Lino Logos (:memory:)") 
DATABASES['default']['NAME'] = ':memory:'

