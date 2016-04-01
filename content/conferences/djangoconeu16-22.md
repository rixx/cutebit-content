Title: DjangoCon Europe 2016 - Beyond Web 2.0 - Django and Python in the modern web ecosystem
Date:   2016-04-01 00:01
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk Beyond Web 2.0 - Django and Python in the modern web ecosystem

**Speaker:** Russell Keith-Magee ([twitter](https://twitter.com/freakboy3742)) is a Django core developer and was the
president of the Django Software Foundation for five years. Also, founder of BeeWare and CTO of TradesCloud.


Over the last five years, peoples' expectations of software has changed dramatically. Let's discussed how this is going
to continue.

## Change of Requirements

Django was released in 2005, when web pages were pretty simple, and the requirements were pretty simple, too.
Django reflects that with its rather simple structure. 2005 the most exotic part of a system would be memcached.

2016: Validation needs to be everywhere, APIs, Forms, Browser. And that's only in the web, but users want Apps.
And Users want updates, so we take websockets, and … yeah. Our structure is pretty broken.

This is also reflected in JS frameworks: from jQuery to Angular …
But a complex client side js framework doesn't fix your problem, it makes it worse: now you have to maintain two complex
frameworks!

## Isomorphic Javascript Development

Idea: Avoid duplication by using the same code on client and server. Meaning javascript on the server. But how do we do that with
Python? Some JS framworks will aim to help you by integrating, but it leads to a lot of duplication. That doesn't sound
right or elegant.

JS's only advantage is that it's native in the browser, and that's a case of Hammer -> Nail if there ever was one.
But! Now we have extra-tooling in any case, because of mobile apps.

## Isomorphic Development (without Javascript): Requirements

Validation on many parts:

 - Server has data. We want to manipulate it and provide it to a client.
 - Clients want access to data and might want to modify it.
 - Mobile devices want the same

Well well well, last time, we solved this with MVC.

## API-first development

Don't use Forms, submit and validate via API.

 - Better testability!
 - Make everyone a priority by providing a rich API

High latency connections or no connections at all - how do we deal with that? We should replicate some or all controller
logic in the client - how do we replicate Python in the browser (and everywhere else)?

## Python in the Browser

Brython, Skulpt and PyPy.js all make Python work in the browser (PyPy is large and uses asm.js).
They are all fairly large - makes stuff slow as hell. It's not efficient. We move a full python parser and interpreter and REPL …

But we don't actually need that, we just want a runnable version of the code. Can we take Bytecode /.pyc to the browder.
**Batavia** is an implementation of the Python runtime without anything else, just implementing the ~100 basic op codes.
It's small!

```python
    def clean(bla):
        return bla.lower()
    clean.__code__
    clean.__code__.co_code

    import base64
    base64.encodebytes(clean.__code__.co_code)
```

Soo, now whe have python in the DOM. Even with DOM modification (`import dom`).
It's not fast, but does that matter? Is it fast enough? It's only got to be fast enough for one user, because it will only
ever have one user.

## Unexpected consequences

Mobile development just got a lot easier! We just don't use the DOM, we use some other API and get very very close to a
single-platform application, because we actually can write mobile apps in Python.
Because Native iOS apps run on ObjectiveC, which is just a cheap C wrapper, and provides ctypes, which we can use from
Python. And we can write a Python class that wraps any Objective-C API. This is what **Rubicon** does.

Android is a bit more complicated. It, too, has C below, but you can't easily reach it. 4.5k references need to be held
for a Hello Wold, but you can only hold 2k references. That's not impossible but … well, it's hard. Enter **VOC**:
Bytecode is a stack-based virtual machine, just as Java Byte code.
VOC translates Python files' Bytecode to Java Bytecode, with line-number translations.

## Now use the same code base

 - **Kivy:** Draws it's own widgets. Great for games, but doesn't produce native apps. Bit fiddly, but mature.
 - **Toga:** Uses native widgets under the hood, but provides a common API. Very much experimental, but it's really easy to
set up.

… can we use Toga for the web, too? Add a Toga backend for Web … ? Yeah, he did it.

## https://freakboy3742.pythonanyware.com

That is a good beginning:

 - we have channels
 - we have mature Django for backend/API
 - it's possible, but possible ain't enough
 - it needs to be the recommended, obvious solution
 - challenge to community: make us not overlooked.
 - success: when web page with app and integrated chat can be done in 15 minutes, instead of, say, a blog
 - django needs to adapt to all of these changes

## contact and links

 - https://cevinestpasun.com
 - https://pybee.com
 - [@freakboy3742](https://twitter.com/@freakboy3742)
 - [mail](mailto:russell@keith-magee.com)

Botavia was a sailing ship from the Netherlands. Mutiny happened, they wanted to run away to Indonesia/Java, but
they sunk.
