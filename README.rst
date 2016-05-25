==========================
lino-logos README
==========================

A Lino application for managing bible editions

Description
-----------

Lino Logos is a `Lino <http://www.lino-framework.org>`__
application for discussing about bible verses.

It is one of the two prototypes which I wrote for the SacredPy
project. (The other prototype is
`Lino Polly <http://lino-framework.org/polly/>`_.)

The central project homepage is http://logos.lino-framework.org



TODO:

-   Decide how data is being imported. Which format to use.
    Think about concordances, formatting tags,...
    I believe that `.usfm` files is currently the best.
    But `.usfm` is quite complex.
    I am just a hobby theologian after all.
    Compare with `OEB
    <https://github.com/openenglishbible/Open-English-    Bible/blob/master/final-usfm/cth/01-Genesis.usfm>`_
    et al.


    And I discovered only now that openenglishbible.org also features other
    editions (Greek and Hebrew).

    This raises new questions.

    Instead of reinventing the wheel and writing a Lino application which
    renders a collection of bible editions into yet another user interface,
    shouldn't you work together with Russell to add interactivity (comments,
    polls, votes...) and other languages to his existing site? Aren't there
    similar projects in other languages? German? Estonian? French? Shouldn't
    they also join?

    Russell did so much work, and he is basically right: he maintains one
    set of files in a "source format" which contains lots of information,
    which he publishes on github, and which he renders to different other
    formats, including .html for mobile or desktop and so on. After all a
    bible edition is a rather static text...

    The only problem with Russell's approach (AFAICS the reason why you
    didn't join him so far) is that *editing the source files* needs rather
    specialized skills. You must be a Python programmer to have a chance to
    learn how to use those tools contained in his github repository. This in
    turn leads to the situation that only a small circle of "privileged"
    people are able to summarize the comments, posts and votings and apply
    them to "our" bible, which after all is the one and only result of our
    collaborative work.

    But this problem is not easy. If we want to solve it, we must be better
    than Russell *and* the Wikipedia. I personally am crazy enough to
    consider trying, but I no longer believe that it will be a quick shot.




Read more on http://logos.lino-framework.org
