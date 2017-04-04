Title: DjangoCon Europe 2017 - Data internationalization in Django
Date:   2017-04-04 01:22
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Data internationalization in Django"

**Speaker:** Raphael Michel

Internationalization in general is already handled very well by Django for static data, but i18n dynamic/user data needs
to be added via third-party libraries. There are about 18 of these, of which 6 appear actively maintained:

- django-hvel
- django-modeltranslations
- django-klingon
- django-i18nfield
- django-parler
- django-cece


### Models

1. Separate fields on the same table: Migrations per new language (modeltranslations)
2. Translation table via foreign key per model: Filtering is harder due to joins (parler, hvad, klingon: separate table
   for *all* translations)
3. Compound field: either be postgres specific or lose ability to filter (nece, i18nfield)

### Fields

1. Custom Base class (either via a special field class or a Meta class attribute) (paerler, hvad, klingon, nece)
2. Custom field type (i18nfield)
3. Registration based: Feels complex, but allows you to integrate third-party apps (modeltranslations)

### Instances

1. Handle one language at a time (via explicit call or context) (parler, hvad, nece)
2. Handle all at once (eg via lazy evaluation or generated per-language attributes) (modeltranslations, i18nfield)
3. Handle only the default language, and every other language explicitly at all times (klingon)

They also differ in filtering, forms support, and db support (nece only works with postgres). Notable are klingon and
i18nfield's disability to filter well, and the excellent form support in modeltranslations and i18nfield. Admin support
is fairly easy to implement in all of these except nece, which seems to lack any documentation on how to display
anything else than just the JSON data. Performance does not vary wildly.
