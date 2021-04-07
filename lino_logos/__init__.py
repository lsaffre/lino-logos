# -*- coding: UTF-8 -*-
## Copyright 2013-2017 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""This is the main module of Lino Logos.

.. autosummary::
   :toctree:

   lib
   projects


"""


import os

from .setup_info import SETUP_INFO

__version__ = SETUP_INFO['version']

intersphinx_urls = dict(docs="http://logos.lino-framework.org")
srcref_url = 'https://github.com/lsaffre/lino-logos/blob/master/%s'
doc_trees = ['docs']
