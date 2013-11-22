"""
Examples how to run these tests::

  $ python setup.py test
  $ python setup.py test -s tests.DocsTests
  $ python setup.py test -s tests.DocsTests.test_debts
  $ python setup.py test -s tests.DocsTests.test_docs
"""
from unipath import Path

ROOTDIR = Path(__file__).parent.parent

# load  SETUP_INFO:
execfile(ROOTDIR.child('lino_logos', 'project_info.py'), globals())

from djangosite.utils.pythontest import TestCase


class BaseTestCase(TestCase):
    demo_settings_module = "lino_logos.settings.demo"
    project_root = ROOTDIR


class DemoTests(BaseTestCase):
    """
    $ python setup.py test -s tests.DemoTests.test_admin
    """
    def test_admin(self):
        self.run_django_manage_test()


class DocsTests(BaseTestCase):
    def test_bibles(self):
        return self.run_docs_doctests('tested/bibles.rst')


class PackagesTests(BaseTestCase):
    def test_packages(self):
        self.run_packages_test(SETUP_INFO['packages'])
