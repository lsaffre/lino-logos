# -*- coding: utf-8 -*-
# Copyright 2013 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""
"""

from lino.api import dd, rt


def objects():

    Book = dd.resolve_model('bibles.Book')

    def book(ref, en, abbr_en, de, abbr_de, et, abbr_et, **kw):
        kw.update(dd.babel_values('name', en=en, de=de, et=et))
        kw.update(dd.babel_values('abbr', en=abbr_en, de=abbr_de, et=abbr_et))
        return Book(ref=ref, **kw)

    yield book("genesis",
               "Genesis", "Gen",
               "Genesis", "Gen",
               "Esimene Moosese raamat", "1Mos")
    yield book("exodus",
               "Exodus", "Ex",
               "Exodus", "Ex", "Teine Moosese raamat",
               "2Mos")
    yield book("leviticus",
               "Leviticus", "Lev",
               "Leviticus", "Lev",
               "Kolmas Moosese raamat", "3Mos")

    yield book("matthew",
               "Matthew", "Mt",
               "Mattäus", "Mt",
               "Matteuse", "Mt")

    from lino_logos.lib.bibles.fixtures.eng_kjv import objects
    yield objects()

    from lino_logos.lib.bibles.fixtures.eng_oeb import objects
    yield objects()

    from lino_logos.lib.bibles.fixtures.est_eps import objects
    yield objects()

    #~ from lino_logos.lib.bibles.fixtures.ger_einheits import objects
    #~ yield objects()

    # from lino_logos.lib.bibles.fixtures.ger_eb import objects
    # yield objects()
