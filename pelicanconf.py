#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'rixx'
SITENAME = 'cutebit'
SITEURL = 'http://cutebit.de'

THEME = "themes/cutebit"

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

PLUGIN_PATHS=["/usr/share/webapps/cutebit.de/plugins"]
PLUGINS=["i18n_subsites"]

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
I18N_SUBSITES = {
	'de': {
		'SITENAME': 'cutebit',
		'LOCALE': 'de_DE.utf8', #This is somewhat redundant with DATE_FORMATS, but IMHO more convenient
	},
}

HIDE_UNTRANSLATED_CONTENT=True

languages_lookup = {
	'en': 'English',
	'de': 'Deutsch',
}

def lookup_lang_name(lang_code):
	return languages_lookup[lang_code]

def my_ordered_items(dict):
	items = list(dict.items())
	# swap first and last using tuple unpacking
	items[0], items[-1] = items[-1], items[0]
	return items

JINJA_FILTERS = {
	'lookup_lang_name': lookup_lang_name,
	'my_ordered_items': my_ordered_items,
}

# Stuff that wasn't in the default config
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_DATE_FORMAT = '%d %B %Y'
DEFAULT_CATEGORY = 'Science'
DEFAULT_DATE = 'fs'
DEFAULT_METADATA = ()
IGNORE_FILES = ['.#*']
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']
TYPOGRIFY = True

INDEX_URL=''
INDEX_SAVE_AS=INDEX_URL+'/index.html'

#ARTICLE_URL='posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_URL='articles'+'/{slug}'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
ARTICLE_SAVE_AS=ARTICLE_URL+'/index.html'

PAGE_PATHS=['pages']
PAGE_URL= PAGE_PATHS[0]+'/{slug}'
PAGE_SAVE_AS = PAGE_URL+'/index.html'

AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'

DEFAULT_ORPHANS = 3
DEFAULT_PAGINATION = 8

CONTACTS = (('Twitter', 'https://twitter.com/codingrixx'),
      ('Stack-Overflow', 'http://stackoverflow.com/users/982635/rixx'),
      ('GitHub', 'https://github.com/rixx'),)
CONTACT_EMAIL = 'rixx-cutebit@cutebit.de'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('blog', INDEX_URL),
	 ('projects', 'projects'),
	 ('cv', 'cv'),
	 ('about', 'about'),
	 ('contact', 'contact'))

