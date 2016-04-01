Title: DjangoCon Europe 2016 - Lightning Talks Day 3, Part 2
Date:   2016-04-01 00:08
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 Lightning Talks Day 3, Part 2


## Daniel: IoT

Real-time two way communication open for long amounts of time with Django. Like the IoT talk, but add more real-time.

Use twisted! It's async and handles protocols for us. But how do we call Django from the async tasks? Do more things
immediately in the workers! It's nice and flexible. Use result and input queues.

Twisted is not Django, and with Channels you will need it less often, but sometimes it's necessary, and now you've seen
how.

## Iacoppo: Desktop Notifications using Channels with Django Knocker

Send notificaitons for changes/additions.

 - install knocker
 - configure channels
 - add two mixins

Logic:
 - listen for signals
 - decide if you need to send a notification
 - create data package
 - send message to a group

## Marysia: Newbie going for an interview

People have strange expectations of Juniors:

 - Juniors are fluent.
    - nope, that comes with practice
 - Juniors have good foundations.
    - nope, that comes with experience or formal education
 - Juniors studied CS
    - nope, not at all, many people cross over to programming

What to do instead? Think of language exams:

 - reading comprehension
 - code manipulation
 - give time to prepare, or tasks for at home

## Russel: TimTam

Australian Biscuit: 2 slices of chocolate biscuit filled with chocolate cream and covered with chocolate.
Mostly for depressed angsty teenagers.

Instead: bite corners diagonally off, and then suck coffee through the middle of the biscuit.
But if you take too long, the biscuit will disintegrate.

## Marko: image-diet2 & pyimagediet
markos.gaivo.net

Page loading wastes users' time, stop doing that.

 - `pip install image-diet2`
 - install external compression tools
 - create config
 - add to `settings.py`
 - configura as `DEFAULT_FILE_STORAGE`

If you're not on Django, use `pyimagediet`, usage is basically the same.

## Idan: API design

Workflow:

 - split up content into cleanly separated resources (close to your models)
 - version your API
 - design clean API
 - then you add parameters
 - first breaking change + bumping version number
 - but you can't delete old versions, so you maintain them forever
 - and you'll have to add new features forever

GraphQL

 - strongly-typed declarative query language
 - kind of functional
 - 'like JSON with the values removed, and then you get a JSON with the values filled in'
 - great for low-memory
 - endpoints: `/graphql`, and that's it
 - you can send more than one command with one request
 - there is a python implementation
 - you can also do joins over *databases*


## Mark: PostgresQL full text search

What is full text search?

 - blocks of text
 - understands language
 - stop words (erm, uh, like)
 - stemming (similar words)
 - relevance

Why?

 - no additional dependency for search, postgres just works
 - strong integration with relational data

Django:

 - nearly done, in final review
 - ` Talk.objects.filter(transcript__search='stroopwafels')`
 - add in SearchVectors to combine queries and annotate with a rank

Performance:

 - cool with ~100s
 - add functional indexes
 - query a trigger updated column

contrib.postgres kickstarter is finished with this patch!

## Milan: async/await

Coroutines:

 - functions whose execution you can pause
 - like generators
 - yield from (Python 3.3 allows chaining generators)

Event Loop:

 - added in Python 3.4, asyncio
 - when X happens, do Y (like onclick)

**Decorator method:** just declare generator as a coroutine
**async/await (since 3.5):** this is not just syntactic sugar. Differentiates between generators and generators meant to be used in
a co-routine.

async/await is not asyncio, it's an API. provides you with building blocks w/o tying the developer to a specific event
loop (like the faaast curio event loop)

async/await is the future: Drop in low-level details, and it's much easier than threading.
