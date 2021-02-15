# how to run a single test:
# $ python -m unittest tests.test_demo.Main.test_algus1

from lino.utils.pythontest import TestCase


class Main(TestCase):

    def do_test_demo_project(self, prjname):
        """Run :manage:`test` and :manage:`demotest` in a subprocess in the given demo project.
        """
        pth = 'lino_logos/projects/' + prjname
        self.run_django_manage_test(pth)
        self.run_django_admin_command_cd(pth, "demotest")

    def test_amici1(self):
        self.do_test_demo_project('sacred')
