===========================
The idea behind Lino Logos
===========================

In october 2013 I read Catherine Devlin's 
blog post `SacredPy seeking collaborators
<http://catherinedevlin.blogspot.com/2013/10/sacredpy-seeking-collaborators.html>`_,
later I had a 30 minutes phone call with Kai Schraml. 
This was the beginning of Lino Logos.

Catherine wrote:

    The need is for a platform into which we can

    - Upload texts in their original language
    - Let users suggest translations for the text, verse-by-verse
    - Debate and discuss the suggestions
    - Vote on them
    
I'd like to add some observations of mine: sacred texts (e.g. the 
Christian bible) and law texts have certain things in common:

- Their message is rather deep and complex.
  They are fruit of the experiences of many people.
- They are collaborative work of many authors.
- They exist in different versions and languages.
- They evolve and change. Not because their message changes but because 
  the readers and their languages change.
- Every single chunk of them is potentially source of a lot of discussion.
- They are not (or should not be) private property of some person or group.

I see a common need for a database application that helps to manage 
such texts.

Wikipedia is probably the first candidate that drops into mind.
The problem with Wikipedia is that it is not designed to work with 
structured data. Okay they are doing a lot of very interesting work 
into this direction, and maybe that's the direction to go. 
But as the author of Lino I was tempted to try my own approach.

Christian bibles however also have some particularities which 
differentiate them from modern law texts:

- They have a canonical structure which uses "books", "chapters" and 
  "verses". This structure didn't change for over 1000 years
  and we are not going to change it.
  
- The canonical structure has no headers, 
  but most editions add headers to give a meaningful structure. 
  These headers don't necessarily respect the canonical chapters.

- (And I discovered more subtleties when diving into this project.)
