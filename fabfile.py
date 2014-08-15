from atelier.fablib import *
setup_from_project('lino_logos','lino_logos.settings.demo')

#~ env.demo_database = 'lino_welfare.demo.settings'

#~ env.demo_databases.append('lino_logos.settings.demo')
#~ env.django_databases.append('userdocs')
#~ env.tolerate_sphinx_warnings = True

#~ env.languages = 'en fr nl'.split()

env.use_mercurial = False  # i.e. use git
