Title: DjangoCon Europe 2016 - Lightning Talks Day 3, Part 1
Date:   2016-04-01 00:01
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 Lightning Talks Day 3, Part 1


## Mark (core): Django Under The Hood

Django Under The Hood on 3rd to 6th November this year.
DUTH is more technical, two days of sprints this year(!), in Amsterdam with logs of Stroopwafels, and dives deep into the ORM.
Go follow [them](https://twitter.com/djangounderhood), or [look](https://djangounderthehood.com) at them.

## Dmitri (jetbrains): Type Hinting

Type Hinting is defined by PEP 484 (Guido), got into Python 3.5. You can specify the type of arguments and return
values. Type Hinting doesn't enforce typing, but does help linters.

For Python 2, you can add type comments with basically the same syntax. But adding type hinting to million lines of code
manually is just not practical.

Feature in PyCharm: look for "python debugger" settings and check the type hinting setting. Basically run tests, so
PyCharm will learn what types are used in functions, and then you can just Alt+Enter on a method to add type hinting
comments! You can even add on Inspection by Name to see where you are still missing Type Annotations.


## Nicole: 6 Ways to Make Tutorials More Beginner Friendly (@oboechick_)

Help against being overwhelmed or stuck in Workshops and Tutorials.

1. Don't use 'easy', 'fast', 'simple': this just needlessly frustrates people and makes them think that they are stupid.
2. There is no question that's stupid or boring. Answer and encourage questions!
3. Many beginners don't think to Google first - don't expect it, but teach them.
4. Don't assume a shared vocabulary - explain your words!
5. Break it down more than you think you need to. Less information/instructions per page.
6. Always have a back-up plan! Plan for internet failure, bring thumb-drive with sources etc.


## Sheryll Transcribing

Program: text on top
Press chords on specialized keyboards (Palantype, Stentura), originally with tape attached, with specialized layouts.
You press keys in combination, like playing a piano.
Also combinations for frequent words, paragraphs, etc. The proceedings may also be recorded and synced with the typed
version, so that you can jump to a location in the text and re-listen to the proceedings.
You may also define dictionaries, for example for Speaker names, technical terms etc.

The software also recognizes recurring terms and shortens them together and creates new shortcuts!It also hints what you
could have written, so that you are able to learn the shorter versions.

## Maikel (mediamoose): Docker

Use docker! Use docker in production! This will make your life better: Dockerize your app from stage to dev to
production.

Use `docker-compose`, and other compose files: `docker-compose.yml`, `docker-compose-staging.yml` etc with

- **overrides**. This kind of sucks because with overriding, you can't remove images or stuff, and have to hack in a busybox to override unused images. 
    - Fewer files, reuse links :)
    - but more implicit, needs busybox hack, longer docker compose command :()

**or**

 - **extends:**: 
    - requires a base file and redefines links :\
    - but more explicit and shorter dc command :)

## Daniel: Things about Django

1. It's crazy (and documented):
    - ForeignKey('self', on_delete=models.CASCADE) for self-referentials
2. It's organized (and documented):
    - write custom django-admin commands
    - write custom managers
3. It's got your back (and documented):
    - try to type in common passwords
    - look up validators

## Emanuelle: Requirements for the Django+Ember workshop

follow the [instructions](http://bit.ly/djember_cc)

Also install Ember inspector and the Django Debug Panel.

## Akos: Responsible DDoS

The Swiss-Cheese-Model: overlapping holes in layered projects can really break everything. While writing an Admin View,
it wouldn't work for the largest group and made a request timeout. Actually, it killed the Django process. Well,
actually, it killed *four* Django processes because there was a request multiplier in between.

Solution:

1. Make sure users cannot do that
2. Turn of request multiplier
3. Isolate issue
4. Fix issue

In reality, there was a slow, large serializer that grew too large for its docker container.

## Daniele: Django in Namibia

 - 63 Namibian students
 - 32 Django Girls
 - 118 attendees
 - very diverse
 - economically complicated, so budgeting was tricky
 - television, radio, newspaper coverage
 - Daniele is Python Software
 - complete conference with talks and workshops
 - large programme, sometimes dual-track
 - lightning talks about hippopotamus safety
 - 50 raspis
 - student protests happened: 45 minutes to find new venue with catering and AV and support
