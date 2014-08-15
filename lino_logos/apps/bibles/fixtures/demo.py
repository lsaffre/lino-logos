# -*- coding: utf-8 -*-
## Copyright 2013 Luc Saffre
## This file is part of the Lino project.
## Lino is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## Lino is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with Lino; if not, see <http://www.gnu.org/licenses/>.

"""
"""

from lino import dd


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

    from lino_logos.apps.bibles.fixtures.eng_kjv import objects
    yield objects()

    from lino_logos.apps.bibles.fixtures.eng_oeb import objects
    yield objects()

    from lino_logos.apps.bibles.fixtures.est_eps import objects
    yield objects()

    #~ from lino_logos.apps.bibles.fixtures.ger_einheits import objects
    #~ yield objects()

    # from lino_logos.apps.bibles.fixtures.ger_eb import objects
    # yield objects()

