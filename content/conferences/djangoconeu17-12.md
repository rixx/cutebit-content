Title: DjangoCon Europe 2017 - Qualities of great reusable Django apps
Date:   2017-04-03 01:12
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Qualities of great reusable Django apps"

**Speaker:** [Flávio Juvenal da Silva Junior](https://twitter.com/flaviojuvenal)

## The concept

- A Django app encapsulates a project feature
- A Django project is mad up of multiple apps
- Reusable apps can be used in multiple projects
- Django encourages multiple apps
- Each app should "Do one thing, and do it well"
- Check that your app's description fits a few words

## Features: Easy to install

- Make it available on PyPI
- Name it `django-*`
- Check for name clashes
- Use wheels
- Add a license
- Publish it on Django Packages
- Maintain dependencies in `install_requires` in `setup.py`
- Check if you need to be a Django app or just a Python package
    - Python packages are easier to use and configure, and may also rely on Django
- Have sane and smart defaults
- Have declarative settings for easy configuration with a custom prefix
- Provide default views with URLs
- Do not rewrite migrations
- Keep a changelog
- Have loud deprecations before removal
- Follow semantic versioning

## Features: Easy to use

- Provide documentation, maybe even write docs first, to think from a user perspective
- Provide a quickstart tutorial
- Separate high level from low level docs
- Use inclusive language
- Provide an example project
- A good documentation is not an excuse for a bad API
- Therefore: Recognition rather than recall: stick with intuitive Django abstractions and interfaces
- Raise `ImproperlyConfigured` if the developer makes a mistake in the config
- Raise `TypeErrors` or similar on errors

## Features: Easy to integrate

[Strive for reusability](https://www.youtube.com/watch?v=ZQ5_u8Lgvyk) (beware, youtube).Strive for great continuity in
the ways in which to extend your project (not just very high-level and very low-level ways).

- Keep separation of concerns
- Break down into portions
- Break class behaviour into methods, resulting in more ways for customization
- Respect the configurability of class-based views
- Break views into mixins
- Leave presentation logic in template tags, move rest into helpers
- Break reusable model parts into abstract models
- Break model filter logic into queryset methods

## Refer to [djangoappschecklist.com](https://djangoappschecklist.com) for reference.
