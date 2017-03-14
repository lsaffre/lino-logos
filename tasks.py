from lino.invlib.ns import ns
ns.setup_from_tasks(
    globals(), "lino_logos",
    tolerate_sphinx_warnings=False,
    blogref_url= 'http://luc.lino-framework.org',
    revision_control_system='git',
    cleanable_files=['docs/api/lino_logos.*'],
    demo_projects=['lino_logos.projects.sacred.settings.demo'])

