## Copyright 2013-2015 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)


import re

from lino.api import dd, rt

Section = dd.resolve_model('bibles.Section')
Verse = dd.resolve_model('bibles.Verse')
VerseText = dd.resolve_model('bibles.VerseText')
Edition = dd.resolve_model('bibles.Edition')

bibles = dd.resolve_app('bibles')

VERSE_RE = re.compile(r"\s*(\d*\S*)\s+(.*)")


class Loader(object):
    current_section = None
    #~ current_chapter = None
    current_book = None
    current_edition = None

    def edition(self,language,abbr,name):
        self.current_edition = Edition(name=name,language_id=language,abbr=abbr)
        self.current_section = self.current_book = None
        return self.current_edition

    def set_book(self,ref):
        #~ self.current_book = bibles.Books.get_by_name(ref)
        self.current_book = bibles.Book.objects.get(ref=ref)

    #~ def chapter(self,title):
        #~ self.current_chapter = Section(title=title,parent=self.current_book)
        #~ self.current_section = self.current_chapter
        #~ return self.current_chapter

    def subsection(self,title):
        return self.section_(title,parent=self.current_section)

    def section(self, title):
        """
        Terminate current section and start a new one at
        the same level.
        """
        if self.current_section is None:
            return self.subsection(title)
        return self.section_(title, parent=self.current_section.parent)

    def section_(self,title,**kw):
        self.current_section = Section(
            title=title,
            edition=self.current_edition,**kw)
        return self.current_section

    def end_section(self,title=None):
        if title is not None:
            assert self.current_section.title == title
        self.current_section = self.current_section.parent

    def parse_line(self, chapter, ln, verse):
        mo = VERSE_RE.match(ln)
        # http://docs.python.org/2.7/library/re.html#re.MatchObject
        if mo is None:
            return verse, ln
        if len(mo.groups()) != 2:
            return verse, ln
            # raise Exception(20131120)
        verseno, text = mo.group(1, 2)
        # print 20131120, verseno, text

        # lns = ln.strip()
        # if not lns:
        #    return None, None

        verse_kw = dict()
        #verseno,text = lns.split(None,1)

        if verseno:
            try:
                verseno = int(verseno)

            except ValueError:
                # only a one-letter suffix is supported, e.g. "11a" or "11A"
                verse_kw.update(verseno_suffix=verseno[-1:].lower())
                try:
                    verseno = int(verseno[:-1])
                except ValueError:
                    verseno = None

        if verseno:
            verse_kw.update(verseno=verseno)
            verse_kw.update(chapter=chapter)
            verse_kw.update(book=self.current_book)

            try:
                verse = Verse.objects.get(**verse_kw)
            except Verse.DoesNotExist:
                verse = Verse(**verse_kw)
                verse.full_clean()
                verse.save()

        return verse, text

    def verses(self,chapter,verses):
        verse = None
        chapter = int(chapter)
        for ln in verses.splitlines():
            verse,text = self.parse_line(chapter,ln,verse)
            if verse and text:
                yield VerseText(verse=verse,
                    edition=self.current_edition,
                    section=self.current_section,
                    text=text)


loader = Loader()
set_book = loader.set_book
edition = loader.edition
#~ chapter = loader.chapter
section = loader.section
end_section = loader.end_section
verses = loader.verses


# __all__ = ['set_book','edition','section','end_section','verses']
