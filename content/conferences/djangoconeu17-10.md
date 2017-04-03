Title: DjangoCon Europe 2017 - Radio Free Django - Building a radio station on Django
Date:   2017-04-03 01:10
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Radio Free Django - Building a radio station on Django"

**Speaker:** Mark Steadman

## Requirements

- Django powered website ('cause it's great, and has great media management, and is hostable on Heroku)
- Automated schedule (which is more complex than it sounds)
- Pages per show and presenter
- Provides a listen-again archive
- Easy to maintain
- Constantly changing homepage

## Scheduling

- Models for `Programme` and `Presenter`
- Handle scheduling via weekday time fields (e.g. 14 fields in the model)
- Handle recurrence and next-air date separately
- Include hiatuses aswell
- Provide programmes running now and next
- To be released on GitHub

## Playback

- Uses MixCloud (also in Django) for listen-again service
- Hack around not-quite-the-same titles by providing fuzzy search

## Recording

- One PC to record dozens of live shows per week
- Overlapping shows? Yeah …
- Send to dropbox, trim, insert artwork, upload to MixCloud
- To be enhanced

## Lessons Learned

- Be prepared to deal with egos
- People want both ease-of-use and ultimate control
- Everybody wants a say
- Scheduling is not easy
