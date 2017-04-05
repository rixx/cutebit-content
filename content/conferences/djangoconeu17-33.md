Title: DjangoCon Europe 2017 - Solidarity of Systers
Date:   2017-04-05 01:33
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Solidarity of Systers"

**Speaker:** Khushbu Parakh (Django Girls coach)

Approximately 150 illion girls under the age of 18 suffer from some sort of sexual violence per year. Solidarity of
Systers provide possibility to get help from members, report past experiences, or share current experiences. The SOS
chat provides contact to lawyers, docters, and NGOs.

This app is written in Django, with a focus on confidential reporting for users - the security and safety of the users
and their data is paramount!

Tools used are postgres, firechat, zxcvbn, Django, and FOX (Federated kOwledge eXtraction framework). It extracts
keywords from text via ensemble learning.

Organization doxxing is an increasingly popular method of attacking organizations like this, and it's not getting any
better. This makes informational security even more important. See for example the most recent WikiLeaks problem.
ZXCVBN is used to estimate password strength, and enforce good passwords.

The workflow is: submit a story, consult on firebase if wanted, receive legal advice, then take action.
The project is hosted on a cloud platform.

The current status is about two days away from open sourcing. They have just become a real official NGO - help on
working on this application is appreciated.
