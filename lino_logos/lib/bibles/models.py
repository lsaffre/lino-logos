# -*- coding: UTF-8 -*-
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
The `models` module for `lino_logos.lib.bibles`.

"""

from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

import os
import datetime

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.exceptions import MultipleObjectsReturned
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat
from django.utils.encoding import force_text 
from django.utils.functional import lazy

from lino.api import dd
from lino import mixins

from lino.modlib.comments.mixins import RFC
from lino.utils import AttrDict
from lino.utils.xmlgen.html import E


def headertag(level):
    tagname = "h" + str(level)
    return getattr(E, tagname)

#~ contacts = dd.resolve_app('contacts')
#~ countries = dd.resolve_app('countries')
languages = dd.resolve_app('languages')


#~ class Book(dd.Choice):
    #~ abbr = dd.BabelCharField(_("Abbreviation"),max_length=20)
    #~ 
#~ class Books(dd.ChoiceList):
    #~ 
    #~ verbose_name = _("Book")
    #~ verbose_name_plural = _("Books")
    #~ item_class = Book
    #~ 
    #~ @classmethod
    #~ def add_item(cls,value,text,ref,abbr):
        #~ super(Books,cls).add_item(value,text,ref,abbr=abbr)
    #~ 
#~ Books.add_item("101",_("Genesis"),"genesis",_("Gen"))
#~ Books.add_item("102",_("Exodus"),"exodus",_("Ex"))
#~ Books.add_item("103",_("Leviticus"),"leviticus",_("Ex"))


class Book(mixins.BabelNamed, mixins.Hierarchical):
    ref = models.CharField(_("Ref"), max_length=20, unique=True)
    abbr = dd.BabelCharField(_("Abbreviation"), max_length=20)
    

class Books(dd.Table):
    model = 'bibles.Book'
        
    
class Edition(RFC):
    name = models.CharField(_("Name"), max_length=200)
    abbr = models.CharField(_("Abbreviation"), max_length=20)
    language = dd.ForeignKey('languages.Language', blank=True, null=True)
    
    def __unicode__(self):
        return self.abbr
    

class Editions(dd.Table):
    model = 'bibles.Edition'
    detail_layout = """
    abbr name language id
    SectionsByEdition comments.CommentsByRFC
    """
    

class Section(mixins.Sequenced, mixins.Hierarchical):
    
    edition = dd.ForeignKey(Edition)
    title = models.CharField(_("Title"), max_length=200)
    
    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")
        
    def __unicode__(self):
        return self.title
        
    @dd.virtualfield(dd.HtmlBox(_("Preview")))
    def preview(self, ar):
        return E.div(*self.get_html_chunks())
        
    def get_html_chunks(self, level=1):
        h = headertag(level)
        if self.title:
            yield h(self.title)
            level += 1
            h = headertag(level)
            
        #~ for v in Verse.objects.filter(section=self).order_by('seqno'):
        for v in VerseText.objects.filter(section=self):
            yield E.span(v.text)
            
        for s in Section.objects.filter(parent=self).order_by('seqno'):
            for chunk in s.get_html_chunks(level):
                yield chunk


class SectionLayout(dd.FormLayout):
    main = "elements preview"
    elements = dd.Panel("""
    parent seqno id edition
    VerseTextsBySection
    SectionsBySection
    """, label=_("Elements"))
    

class Sections(dd.Table):
    model = Section
    detail_layout = SectionLayout()

    
class SectionsBySection(Sections):
    master_key = 'parent'
    

class SectionsByEdition(Sections):
    master_key = 'edition'
    filter = models.Q(parent__isnull=True)
    column_names = "title"
    auto_fit_column_widths = True
    

class Verse(RFC):
    class Meta:
        verbose_name = _("Verse")
        verbose_name_plural = _("Verses")
        ordering = ['verseno', 'verseno_suffix']
        
    book = dd.ForeignKey(Book)
    chapter = models.IntegerField(_("Chapter"))
    #~ book = Books.field()
    verseno = models.IntegerField(_("Number"), help_text=_("Verse number"))
    verseno_suffix = models.CharField(
        _("Suffix"), max_length=5, blank=True,
        help_text=_("Optional a,b,c behind verse number"))
        
    def __unicode__(self):
        return _("%(book)s %(chapter)d:%(verseno)s") % dict(
            book=self.book.abbr, chapter=self.chapter, verseno=self.verseno)


class VerseText(dd.Model):
    "The text of a given Verse in a given Edition"
    class Meta:
        verbose_name = _("Verse")
        verbose_name_plural = _("Verses")
        
    verse = dd.ForeignKey(Verse)
    edition = dd.ForeignKey(Edition)
    text = models.TextField(_("Text"))
    section = dd.ForeignKey(Section, blank=True, null=True)

        
class VersesParams(object):
    parameters = dict(
        p_edition=dd.ForeignKey(Edition),
        p_chapter=models.IntegerField(_("Chapter"), blank=True, null=True),
        p_book=dd.ForeignKey(Book,blank=True,null=True)
    )
    params_layout = "p_edition p_book p_chapter"

    @dd.chooser(simple_values=True)
    def p_chapter_choices(cls):
    #~ def p_chapter_choices(cls,p_edition,p_book):
        if False:
            # TODO: context for ChoiceListField doesn't yet get passed
            print p_book
            qs = Verse.objects.filter(book=p_book)
            print 20131012, qs.query
            chapters = qs.values_list('chapter',flat=True)
            #~ print 20131012, chapters
            chapters = list(set(chapters))
            return chapters
        return range(1, 99)


class Verses(VersesParams, dd.Table):
    model = Verse
    order_by = ['verseno', 'verseno_suffix']
    detail_layout = """
    book chapter verseno verseno_suffix id
    VerseTextsByVerse:40 comments.CommentsByRFC:20
    """
    #~ column_names = "verseno text"
    

class VerseTexts(dd.Table):
    model = VerseText
    variable_row_height = True

    
class VerseTextsByVerse(VerseTexts):
    master_key = 'verse'
    column_names = 'text edition section'
    auto_fit_column_widths = True
    
#~ class Verses(VersesParams,dd.Table):
    #~ model = Verse
    #~ order_by = ['verseno','verseno_suffix']
    #~ detail_layout = """
    #~ edition book verseno section id
    #~ text
    #~ """
    #~ column_names = "verseno text"
    #~ 
    #~ 
    #~ @classmethod
    #~ def get_request_queryset(self,ar):
        #~ if not ar.param_values.p_edition:
            #~ return []
        #~ qs = super(Verses,self).get_request_queryset(ar)
        #~ if isinstance(qs,list): return qs
        #~ qs = qs.filter(edition=ar.param_values.p_edition)
        #~ if ar.param_values.p_book:
            #~ qs = qs.filter(book=ar.param_values.p_book)
        #~ if ar.param_values.p_chapter:
            #~ qs = qs.filter(chapter=ar.param_values.p_chapter)
            #~ 
        #~ return qs


class VerseTextsBySection(VerseTexts):
    master_key = 'section'
    column_names = "verse text"
    auto_fit_column_widths = True
 
LEFT = _("Left")
RIGHT = _("Right")


class SideBySideVerses(VersesParams, dd.VirtualTable):
    parameters = dict(
        edition1 = dd.ForeignKey(Edition,verbose_name=LEFT),
        edition2 = dd.ForeignKey(Edition,verbose_name=RIGHT),
        p_chapter = models.IntegerField(_("Chapter"),blank=True,null=True),
        p_book = dd.ForeignKey(Book,blank=True,null=True),
        #~ p_book = Books.field(blank=True,null=True)
    )
    
    params_layout = "edition1 edition2 p_book p_chapter"
    auto_fit_column_widths = True
    variable_row_height = True
    
    @classmethod
    def get_data_rows(cls,ar):
        qs = VerseText.objects.all()
        if ar.param_values.p_book:
            qs = qs.filter(verse__book=ar.param_values.p_book)
        if ar.param_values.p_chapter:
            qs = qs.filter(verse__chapter=ar.param_values.p_chapter)
        verses = dict()
        versenos = []
        for obj in qs.order_by('verse__verseno','verse__verseno_suffix'):
            k = obj.verse.pk
            v = verses.get(k,None)
            if v is None:
                versenos.append(k)
                v = AttrDict(pk=k,left='',right='',verse=obj.verse)
                verses[k] = v
            if obj.edition == ar.param_values.edition1:
                v.left = obj.text
            elif obj.edition == ar.param_values.edition2:
                v.right = obj.text
        for k in versenos:
            yield verses[k]
        
    @classmethod
    def get_column_names(cls,ar):
        return "verseno:5 text1 text2"
        
    @dd.displayfield(_("No"))
    def verseno(self,obj,ar):
        return unicode(obj.verse)
        
    @dd.displayfield(LEFT)
    def text1(self,obj,ar):
        return obj.left
        
    @dd.displayfield(RIGHT)
    def text2(self,obj,ar):
        return obj.right


