.. _logos.tested.bibles:

Bibles
=======

.. include:: /include/tested.rst

The following statement imports a set of often-used global names::

>>> from lino.api.shell import *

We can now refer to every installed app via it's `app_label`.
For example here is how we can verify here that the demo database 
has three Sections and four Texts:

>>> bibles.Section.objects.count()
9
>>> bibles.Edition.objects.count()
3

