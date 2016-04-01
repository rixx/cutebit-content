Title: DjangoCon Europe 2016 - How to upgrade to the newest and shiniest Django
Date:   2016-03-31 00:09
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "Going with the Flow with Django Admin"How to upgrade to the newest and shiniest Django""


**Speaker:** Susan Tan ([twitter](https://twitter.com/arctansusan)) at Cisco via Piston, previously at Rotten Tomatoes.
She also works on [openhatch](https://www.openhatch.org).

Upgrades are great because they fix bugs, provide security fixes, new features and make upgrading to even newer versions
easier. Be aware of semantic versioning.

## When to upgrade

Upgrade at patch releases, upgrade when your version is out of support (at the moment, 1.8 LTS and 1.9 are current).
Also, upgrade if you have a comprehensive test suite. If you don't have one, write one.

## Problems and Barriers

 - Uprgrade effort and duration is hard to guess
 - Will tests run?
 - Will UI work?
 - Confirm functionality at every point: 


## Order of Operations

1. Read release notes
2. Dependencies may break, check that
3. Uninstall old version, install new version, upgrade dependencies
4. Make codebase compatible
5. Run and fix tests
6. Check and fix UI

## Don't

Don't skip over versions! You'll miss deprecation warnings and run into invalid code!

