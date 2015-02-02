from atelier.fablib import *
setup_from_fabfile(globals(), 'lino_logos', 'lino_logos.settings.demo')

add_demo_project('lino_logos.settings.demo')

#~ env.demo_database = 'lino_welfare.demo.settings'

#~ env.demo_databases.append('lino_logos.settings.demo')
#~ env.django_databases.append('userdocs')
#~ env.tolerate_sphinx_warnings = True

#~ env.languages = 'en fr nl'.split()

env.revision_control_system = 'git'

