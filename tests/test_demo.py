# how to run a single test:
# $ python -m unittest tests.test_demo.TestCase.test_sacred

from lino.utils.pythontest import TestCase


class TestCase(TestCase):

    demo_projects_root = 'lino_logo/projects'

    def test_sacred(self):
        self.do_test_demo_project('sacred')
