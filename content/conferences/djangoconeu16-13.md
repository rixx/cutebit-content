Title: DjangoCon Europe 2016 - The Power ⚡️ and Responsibility 😓 of Unicode Adoption ✨
Date:   2016-03-31 01:03
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "The Power ⚡️ and Responsibility 😓 of Unicode Adoption ✨"

**Speaker:** Katie McLaughlin ([twitter](https://twitter.com/glasnt)) is an Operations Engineer.

Emojis are broken.

## Origins

ASCII was 7 bit, extended ASCII for Europeans 8 bit, and then we got unicode with 32 bit (or utf-8 for size, since we
only use 10% of unicode space).

## Old Emojis

There was Windings, there was the peace sign, which is in unicode since the 90s, but mostly there were telecommunication
companies' emojis, which were then made consistent by a combined effort of apple and google to introduce emojis into
unicode standard v6.

## Unicode Standards

 - **v6:** Emojis join Unicode (2010)
 - **v6.1:** Faces get added (2012)
 - **v7:** spock gesture, chipmunk, unicorn (2014)
 - **v8:** rock symbol, taco, upside-down smiley (2015)
 - **v9:** selfie, bacon, duck, spoon, whisky, egg (2016)
 - **v10:** more takeaway food (2017)

 ```
 import unicodedata
 unicodedata.name('⚡️')
 ```

## Get Emojis accepted

Emojis are decided on by the Emoji Board of the Unicode Consortium.

**Good:**

 - backwards compatibility
 - frequently used things (substantiated by google trends or similar, compared to, say, hamburgers)
 - distinctiveness from other emoji
 - completeness (eg add missing zodiac signs)

**Bad:**

 - overly specific
 - open-ended categories
 - already represented (even in combination)
 - no branding
 - no fads

## Best Practices
 
 - provide emojis yourself if you want any control over how they look
 - add alt-texts
 - refer to emojis by their standardized name
 - use the twitter set (permissive license) or the emojione set, which is completely open source
