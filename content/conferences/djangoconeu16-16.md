Title: DjangoCon Europe 2016 - Building a non-relational Backend for Django's ORM
Date:   2016-03-31 01:06
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "Building a non-relational Backend for Django's ORM"

**Speaker:** Adam Alton ([twitter](https://twitter.com/altonpowers)) at Potato.

The backend is called Djangae, and is a Django backend for Google's Datastore.

## Why?

Build a Django backend for the Datastore, to build a great and flexible (scaling) application for the Google App Engine.
The Datastore is basically made for Gmail.

## Limitations

The Datastore has these limitations:

 - every query must use and index
    - no table scans
    - maximum of one inequality filter per query
    - no JOINs
 - eventual consistency
 - no schema (updating every row could take days, every row is a dict)
 - transactions must query by pk
 - random auto-generated IDs
 - counting is really, really slow

So, for Django there need to be workarounds for:

 - ManyToMany relations
 - Permissions
 - unique and unique_togeter contraints
 - GenericForeignKey
 - concrete model inheritance
 - transaction.atomic
 - pagination
 - Django admin
 - migrations

## Building a backend

A backend sits between Queries and the actual Database. To build the backend, you have to modify these classes:

 - `DatabaseFeatures`: flags indicating what kinds of stuff the database supports
 - `DatabaseIntrospection` and `DatabaseSchemaEditor`: … just `pass`
 - `DatabaseWrapper`: insert a dummy connector class, because we use an API instad of a connection
    - but a connection has a cursor, which needs to be duck-typed
    - with about 15k LOC
    - and 2.4k commits, 400PRs and 45 people involved
    - the cursor will get an SQL string and the rest is magic

## Challenges and solutions

 - solve the inequality constraint by transforming WHERE queries to their DNF (disjunctive normal form)
 - Django might give you floats, expecting them to be cast to ints (timestamps, specifically), and blow up when it reads
   slightly malformed floats again
 - Tests working with incrementing IDs will overlook a lot of errors if you actually work on a DB with random
   auto-generated IDs
 - implemented unique constraints via an additional unique marker table, with one marker per unique per field per column
 - implemented ManyToMany with repeated properties and a RelatedListField, because it's all a dict anyways
 - use the ManyToMany implementation to form Users and Groups and ultimately a permission system
 - mock and monkeypatch Content Types away
 - implement Concrete Model Inheritance by storing everything in one table with an additional classes column denoting
   the type
 - transactions can't be the same due to primary key constraint, but they can be re-built with their own
   djangae.transaction.atomic decorator
 - pagination is possible, as long as you don't try to return the total. So don't.

## Migrations

Migrations aren't solved yet, because wo don't have ssh, we just talk to a DB API. Migrations can take days on these
amounts of data, but Django has no concept of a migration being in-progress (this is apparently fixed with 1.11?). To
change this on the fly, you would need to change the MigrationRecorder, but you can't run migrations on the
MigrationRecorder (to make the status field nullable, for example), sooo … nope.

