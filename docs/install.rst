.. _logos.install:

Installing Lino Logos
=======================

Development server
------------------

If you need only a development server, 
just install Lino (the framework) as documented 
in :ref:`lino.dev.install`, then:

- Go to your `hgwork` directory and 
  download also a copy of the Lino Logos repository::

    cd ~/hgwork
    hg clone https://code.google.com/p/lino-logos/ logos
    
- Use pip to install this as editable package::

    pip install -e logos

- In your project's `settings.py`, make sure that you inherit from 
  the right `settings` module::
    
    from lino_logos.settings import *


