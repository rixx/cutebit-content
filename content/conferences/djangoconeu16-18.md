Title: DjangoCon Europe 2016 - Django Microservices Made Easy
Date:   2016-03-31 01:08
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "Django Microservices Made Easy"

**Speaker:** Paul Hallett ([twitter](https://twitter.com/phalt_)) works for Lyst.

## Microservices?

Where monolithic applications are a Death Star that manages everything, but if it breaks, everything is broken,
microservices are like a fleet of X-Wing Fighters: they are a fleet of small, independant, highly specialized vehicles

## Problems and Solutions

 - **Shared Databases:** Don't. Isolate and decouple your dependencies.
 - **Inconsistent Project Structures:** write project templates for unified deployment/testing/error logging approaches
   (cookiecutter)
 - **Inconsistent HTTP Interfaces:** Include Clients and [Client
   Guidelines](https://github.com/lyst/MakingLyst/tree/master/api-best-practices)
 - **Consistent Deployment:** Use Empire, a heroku-like interface for deployment

## Next up:

Automate even more, auto-generate even more … and profit.
