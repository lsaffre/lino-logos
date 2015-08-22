# -*- coding: UTF-8 -*-
## Copyright 2013-2015 Luc Saffre
# License: BSD (see file COPYING for details)
"""This is the main module of Lino Logos.

.. autosummary::
   :toctree:

   lib
   projects


"""


import os

execfile(os.path.join(os.path.dirname(__file__),'setup_info.py'))
__version__ = SETUP_INFO['version']

intersphinx_urls = dict(docs="http://logos.lino-framework.org")
srcref_url = 'https://github.com/lsaffre/lino-logos/blob/master/%s'
