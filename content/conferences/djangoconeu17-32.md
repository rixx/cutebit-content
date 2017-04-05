Title: DjangoCon Europe 2017 - Defining a customizable boilerplate using Django, React and Bootstrap
Date:   2017-04-05 01:32
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Defining a customizable boilerplate using Django, React and Bootstrap"

**Speaker:** Lais Varejão

## Boilerplate

Refers to sections of code that have to be included in many places with little of no alteration, e.g. the basic
structure of an HTML document. Using a boilerplate has its uses: it reduces repetition, it speeds up project setup, with
less errors on the way.

It also leads to common project structure, which is a very good thing - you'll be able to work quickly with other
similar projects.

There are, for example, the [HTML5 boilerplate](https://html5boilerplate.com),
[the Django cookiecutter](https://github.com/pydanny/cookiecutter-django), …

## The Django React Boilerplate

It's [open source](https://github.com/vintasoftware/django-react-boilerplate), and uses Django 1.10 with React,
django.js, Bootstrap 4, Webpack, Celery, and WhiteNoise for static file serving.

There are obviously high maintenance costs. It is hard to maintain the boilerplate and keep it updated to the latest
package versions. It *must* be seen as a constantly evolving project.

## What to look for

- Well defined principles
- Componentize to decouple
- Kept simple
- DRY
- Separation of concerns
- Be clear on your feature set
- Be clear on your tech stack
- Do not forget about things like
    - logging
    - performance monitoring
    - pre-commit hooks
    - linters
    - continuous integration
    - continuous delivery
- Separate config for production/development/stage/test
- Find clever ways to deal with shared code

## Framework choices

Django is great for boilerplates since the Django project template is extensible (`django-admin startproject
--template=…`). React is included with npm, babel and webpack. Webpack provides very complex configuration, but also very
cool features, such as hot module replacement.
Bootstrap is just kind of compatible to everything, in terms of framework, css markup etc.

Also contribute to [this boilerplate list](https://awesomeboilerplate.com).
