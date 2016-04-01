Title: DjangoCon Europe 2016 - A Brief History of Channels
Date:   2016-03-31 01:04
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "A Brief History of Channels"

**Speaker:** Andrew Godwin ([twitter](https://twitter.com/andrewgodwin)) is a core developer with Django and a senior
developer at Eventbrite. Also, the author of `channels`.

## `channels`?

Channels is Andrew's initiative to bring websockets to Django. Websockets are 6-7 years old and break the strict HTTP
request-response pattern by allowing both parties to send or receive whenever they want. Websockets are open connections
with unlimited bi-directional communication.

## Goals

 - be hard to deadlock (deadlocks are a common problem with async communication)
 - built-in auth and security
 - easily deployable
 - scaling easily up and down
 - optional

## Solution

Since Django is very much request-based, we'll swap out requests for events when using channels.

A channel is a **named** (identified via string), **first-in-first-out** (ordered), **at-most-once** (failure state is
to drop the message), **non-broadcast** (only one listener will receive the message), **network-transparent** (will work
over a network) queue of messages.

It's bascally breaking Django into two parts: a protocol server handling requests/events, and a worker server handling
business logic.

## Usage

It's included in Django 1.10 and installable (`pip install channels`) for Django 1.8 and 1.9 and will be maintained for
all of these for a while. There is also [extensive documentation](https://channels.readthedocs.com). Even better, there
are **[heavily annotated working examples](https://github.com/andrewgodwin/channels-examples)** - go read them!

You basically write a Consumer instead of a View. A Consumer is very similar (still callable, might be class or function). A consumer receives messages instead of requests, and doesn't return a value, but instead uses `message.reply_channel.send({})`, and that's it.

You can also use per-socket session with `message.channel_session`, and utilize Groups for broadcasting or pub/sub style
communication. You can add and remove channels from a group and send messages to groups.

## Outlook

Channels has even more features not mentioned due to time constraints (replacing wsgi, pluggable backend, sharding and
scaling, and it still works with just `runserver`).
Down the road there might be a scheduler, retry logic, a generic consumer and many other great things.
