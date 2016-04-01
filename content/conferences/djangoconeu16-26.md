Title: DjangoCon Europe 2016 - Safe-Ish by Default: The Django Security Model and How to Make it Better
Date:   2016-04-01 00:06
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk Safe-Ish by Default: The Django Security Model and How to Make it
Better

**Speaker:** Philip James ([twitter](https://twitter.com/phildini)) is a Senior Software Engineer at Eventbrite, who
likes writing bots for Slack and Twitter.


Django does the simplest possible thing that works.

## What actually works

### XSS: Cross-Side Scripting

Django escapes stuff for you - and this has been essentiall unchanged since Django was opensourced.
Don't turn this off.

### CSRF: Cross-Site Request Forgery

Expecially important with forms. Django will look for CSRF tokens and denies POST request with mismatches.
Don't turn this off.

Cookies can be HTTP-only (can only be touched by the server) or not. The Django CSRF cookie is not HTTP-only, so that
you can use the CSRF cookie with js + ajax.

### SQLi: SQL Injections

"Don't ever confuse code and data, it's the key to happiness." - Alex Gaynor.

Django protects from SQLi by keeping code and data separate through the entire ORM, until they meet the database. Don't
turn this off.

### Clickjacking

If somebody puts your site into an iFrame on their side. Django sets an XFrameOptionsMiddleware header which mmmost
browsers respect by not rendering the site if the header is sent.

### Host Header Validation

Django forces Host Header Validation if `debug = False`.

### Sessions & Passwords

Django just does the right things by default, including automatic algorithm upgrades (the next time a user logs in,
Django will authenticate them and then re-hash the password and save it).

## How do we make this better.

**CONSTANT VIGILANCE!**

 - Have checks against workarounds around security measures.
 - HTTPS, seriously
 - CSP Reporting (Set some headers, and browsers will accept that only some content should be loaded/report)

### Third party libs

 - `django_encrypted_fields`
 - `django-secure`
 - [PonyCheckup](https://ponycheckup.com)
 - [amazing talk](http://nerd.kelseyinnis.com/blog/2015/09/08/making-django-really-really-ridiculously-secure/)
