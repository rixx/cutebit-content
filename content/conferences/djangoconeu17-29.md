Title: DjangoCon Europe 2017 - Last Mile Django
Date:   2017-04-05 01:29
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Last Mile Django"

**Speaker:** Tom Wier

## Connectivity

Connectivity is worse, slower, and expensive and hence unavailable to most people
So take care to send less data - overall! Single page applications *might* work better since there is a large first
request, but only small subsequent requests. The single page applications gives you more control in working around slow
connections, too. Consider carefully if this is worth it.

## Languages and literacy

Less people speak English. Internationalize your website. Support major languages at least, but start thinking about
smaller local languages, too. Use gettext. Use translation comments explaining the context. Pay attention to
pluralization, and add context strings (pgettext).

## Incomplete or wrong data

Addresses or locations work differently. See also: [falsehoods programmers believe about addresses](https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/).
You can also use fuzzy input to match places that have no consistent spelling.
