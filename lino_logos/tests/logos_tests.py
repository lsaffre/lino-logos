# -*- coding: utf-8 -*-
## Copyright 2013 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""
This module contains "quick" tests that are run on a demo database
without any fixture. You can run only these tests by issuing::

  python manage.py test lino_logos.QuickTest

"""

from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

import decimal

#~ from django.utils import unittest
#~ from django.test.client import Client
from django.conf import settings

#from lino.igen import models
#from lino_xl.lib.contacts.models import Contact, Companies
#from lino_xl.lib.countries.models import Country
#~ from lino_xl.lib.contacts.models import Companies

from django.utils import translation
from django.utils.encoding import force_str
from django.core.exceptions import ValidationError

from lino.api import dd, rt
from lino.utils import i2d
from lino.utils.djangotest import RemoteAuthTestCase

#~ contacts = dd.resolve_app('contacts')

DEMO_OVERVIEW = """\
10 applications: sessions, about, contenttypes, system, users, changes, countries, contacts, bibles, djangosite.
29 models:
======================================= ========= =======
 Name                                    #fields   #rows
--------------------------------------- --------- -------
 changes.Change                          9         0
 contacts.Company                        23        12
 contacts.CompanyType                    7         16
 contacts.Partner                        19        81
 contacts.Person                         24        69
 contacts.Role                           4         0
 contacts.RoleType                       4         5
 contenttypes.ConcreteModel              2         0
 contenttypes.ContentType                4         29
 contenttypes.FooWithBrokenAbsoluteUrl   3         0
 contenttypes.FooWithUrl                 3         0
 contenttypes.FooWithoutUrl              2         0
 contenttypes.ProxyModel                 2         0
 countries.Place                         8         72
 countries.Country                       6         8
 bibles.Edition                          4         4
 sessions.Session                        3         4
 system.HelpText                         4         2
 system.SiteConfig                       4         1
 system.TextFieldTemplate                6         2
 users.Authority                         3         0
 auth.Membership                        3         0
 auth.Team                              4         0
 users.User                              13        3
======================================= ========= =======
"""


class QuickTest(RemoteAuthTestCase):


    def test00(self):
        """
        Initialization.
        """
        #~ print "20130321 test00 started"
        self.user_root = settings.SITE.user_model(username='root',language='en',profile='900')
        self.user_root.save()


class DemoTest(RemoteAuthTestCase):
    maxDiff = None
    #~ fixtures = 'std demo'.split()
    fixtures = settings.SITE.demo_fixtures

    def test001(self):
        """
        test whether the demo fixtures load correctly.
        """

        s = settings.SITE.get_db_overview_rst()
        #~ print s
        self.assertEqual(DEMO_OVERVIEW,s)
