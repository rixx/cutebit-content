Title: DjangoCon Europe 2017 - Django’s watching my back(end)
Date:   2017-04-03 01:08
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Django’s watching my back(end)"

**Speaker:** [Carlos de las Heras](https://twitter.com/cahersan)

## General

Things have changed since 2003. The scopes and life cycles have changed, new paradigms have appeared, especially with
respect to the request/response cycle.

Moving from template rendering to single page applications is maybe the way to go, providing just a REST API via Django,
handling also identity management Django-side.

The tool chain here includes primarily `restframework`, and `JWT` as auth tokens. Authentication and permission is
completely handled by `djangorestframework-jwt` and decorators/permission classes.

## JSON Web Tokens (JWT)

* stateless authentication mechanism (no session, no cookie)
* signed: can be decoded and checked for validity
* sent via an Authorization header
* can handle expiration, too
* logging in is handled by sending a token to the client which is then added to every further request
* registration is handled as normally, with a confirmation mail
* testing must mock the token

## Integrating angular

* Set CORS headers with django-cors-headers
