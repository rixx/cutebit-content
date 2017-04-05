Title: DjangoCon Europe 2017 - Level up! Rethinking the Web API framework
Date:   2017-04-03 01:05
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Level up! Rethinking the Web API framework"

**Speaker:** Tom Christie (Django core developer and author of Django REST framework)

## Build meaning into codebase

Describe APIs, make them browsable, make clients dynamic, make them self-descriptive and self-documenting.

## Proposed steps

### Routing

Route all requests to an endpoint to one function, but then split up according to e.g. request type.
This allows us to inspect the code and use doc strings of *two* methods for documentation.

### Change the interface

Change the interface: Let the method take readable parameters (e.g. 'user', 'name') instead of a request
object, and return data instead of another request object.

This can be done by pytest style dependency injection into the method parameters.

### Type annotations

Explicitly declared type annotations make assumptions clear to both users (via documentation) and developers.

## JSON Schema

JSON Schema is a machine readable format for describing data structures. It is widely adopted and can be used for both
documentation and validation and has a large range of capabilities.

## Merge those

Create a type systems that maps types on JSON schema while performing validation. Then go on and use those for type
annotations. If you use those with dependency injections: magic happens

## API tooling

1. API mocking: can be done (automatically) as soon as the API is defined. This allows the frontend team start working
   much sooner.
2. Browsable API
3. API documentation can be generated effortlessly, and is guaranteed to be in sync with the implementation
4. Dynamic client libraries can be built schema-driven for various languages (JS, Python, CLI)
5. Exposing your views as management functions
6. Real time APIs: route other protocols to the same views (except that depending on the protocol different magic needs
   to e.g. retrigger the view)

Look at the [ongoing project](https://github.com/tomchristie/apistar).
