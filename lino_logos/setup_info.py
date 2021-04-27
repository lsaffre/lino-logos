# -*- coding: UTF-8 -*-
## Copyright 2013 Luc Saffre

SETUP_INFO = dict(
    name='lino-logos',
    version='0.0.1',
    install_requires=['lino'],
    test_suite='tests',
    description="A Django Lino application for managing bible editions",
    long_description="""\
Lino Logos is a `Lino <https://www.lino-framework.org>`__
application for discussing about bible verses.

It is one of the two prototypes which I wrote for the SacredPy
project. (The other prototype is
`Lino Polly <http://lino-framework.org/polly/>`_.)


TODO:

-   Decide how data is being imported. Which format to use.
    Think about concordances, formatting tags,...
    I believe that `.usfm` files is currently the best.
    But `.usfm` is quite complex.
    I am just a hobby theologian after all.
    Compare with `OEB
    <https://github.com/openenglishbible/Open-English-\
    Bible/blob/master/final-usfm/cth/01-Genesis.usfm>`_
    et al.


    And I discovered only now that openenglishbible.org also features other
    editions (Greek and Hebrew).

    This raises new questions.

    Instead of reinventing the wheel and writing a Lino application which
    renders a collection of bible editions into yet another user interface,
    shouldn't you work together with Russell to add interactivity (comments,
    polls, votes...) and other languages to his existing site? Aren't there
    similar projects in other languages? German? Estonian? French? Shouldn't
    they also join?

    Russell did so much work, and he is basically right: he maintains one
    set of files in a "source format" which contains lots of information,
    which he publishes on github, and which he renders to different other
    formats, including .html for mobile or desktop and so on. After all a
    bible edition is a rather static text...

    The only problem with Russell's approach (AFAICS the reason why you
    didn't join him so far) is that *editing the source files* needs rather
    specialized skills. You must be a Python programmer to have a chance to
    learn how to use those tools contained in his github repository. This in
    turn leads to the situation that only a small circle of "privileged"
    people are able to summarize the comments, posts and votings and apply
    them to "our" bible, which after all is the one and only result of our
    collaborative work.

    But this problem is not easy. If we want to solve it, we must be better
    than Russell *and* the Wikipedia. I personally am crazy enough to
    consider trying, but I no longer believe that it will be a quick shot.


""",
    author='Rumma & Ko Ltd',
    author_email='info@lino-framework.org',
    url="https://github.com/lsaffre/lino-logos",
    license_files=['COPYING'],
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 1 - Planning
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Intended Audience :: System Administrators
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: OS Independent
Topic :: Office/Business :: Scheduling
""".splitlines())

SETUP_INFO.update(packages=[
    'lino_logos',
    'lino_logos.projects',
    'lino_logos.projects.sacred',
    'lino_logos.projects.sacred.settings',
    'lino_logos.projects.sacred.tests',
    'lino_logos.lib',
    'lino_logos.lib.bibles',
    'lino_logos.lib.bibles.fixtures',
    'lino_logos.tests',
])

SETUP_INFO.update(message_extractors={
    'lino_logos': [
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**.js',                'javascript', None),
        ('**/templates_jinja/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(package_data=dict())


def add_package_data(package, *patterns):
    l = SETUP_INFO['package_data'].setdefault(package, [])
    l.extend(patterns)
    return l

add_package_data('lino_logos',
                 'config/bibles/Edition/*.odt',
                 'config/bibles/Verse/*.odt')

l = add_package_data('lino_logos')
for lng in 'fr de nl'.split():
    l.append('locale/%s/LC_MESSAGES/*.mo' % lng)
