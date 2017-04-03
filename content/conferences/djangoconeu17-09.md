Title: DjangoCon Europe 2017 - Staying DRY(er) when working with Django and frontend frameworks/libraries
Date:   2017-04-03 01:09
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Staying DRY(er) when working with Django and frontend frameworks/libraries"

**Speaker:** [Emma Delescolle](https://twitter.com/EmmaDelescolle) (co-author of drf-schema-adapter)

There is drf-schema-adapter. It provides you with a toolset to create fully dynamic frontend clients for your Django
application, for the js framework of your choice.

It provides an `Endpoint` class, similar to the `Admin` class. Can also use DRF viewsets.
It provides a router (via drf_auto_endoint) to register models directly aswell as auto-discovery.

The frontend is provided via an adapter set in the settings, that will produce framework dependend js code. The code
will rely on a common base file (that will be overridden by subsequent updates) and model specific code files (which you
can change without fear of overwriting).

There is also a metadata adapter, providing metadata on relationships, read-only fields etc. With this adapter,
meaningful forms can be generated. You can also build custom adapters, of course. Feel free to play around! Even complex
models and relations are no problem.
