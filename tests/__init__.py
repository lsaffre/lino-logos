"""
Examples how to run these tests::

  $ python setup.py test
  $ python setup.py test -s tests.DocsTests
  $ python setup.py test -s tests.DocsTests.test_debts
  $ python setup.py test -s tests.DocsTests.test_docs
"""
from unipath import Path

ROOTDIR = Path(__file__).parent.parent

# SETUP_INFO = dict()
# execfile(ROOTDIR.child('lino_logos', 'setup_info.py'), globals())

from lino.utils.pythontest import TestCase


class BaseTestCase(TestCase):
    django_settings_module = "lino_logos.settings.demo"
    project_root = ROOTDIR


class DemoTests(BaseTestCase):
    """
    $ python setup.py test -s tests.DemoTests.test_admin
    """
    def test_admin(self):
        self.run_django_manage_test('lino_logos/projects/sacred')


class DocsTests(BaseTestCase):
    def test_bibles(self):
        return self.run_docs_doctests('tested/bibles.rst')


class PackagesTests(BaseTestCase):
    def test_packages(self):
        import lino_logos
        self.run_packages_test(lino_logos.SETUP_INFO['packages'])
