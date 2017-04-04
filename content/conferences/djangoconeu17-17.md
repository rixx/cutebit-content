Title: DjangoCon Europe 2017 - To Index or Not, That’s Not The Question
Date:   2017-04-04 01:17
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "To Index or Not, That’s Not The Question"

**Speaker:** Markus Holtermann (Django core developer with a particular focus on the migrations framework)

## Background theory

Filtering/selecting for a specific value does a full table scan by default. This does not scale for large tables.

DB Indexes give access to a single or multiple column in your table, making guarantees on timing for specific lookups.

Indexes use **B Trees**. B trees are self-balancing, providing us with the timing guarantees.

B Trees have nodes combining several values and several + 1 pointers.
Leaf values then hold a pointer to the table row it belongs to.
The other pointers point to further nodes which hold values smaller,
in-between, and larger than the values in the node, respectively. This provides an easy way to find a value,
binary-search style.

An additional pointer points go to the next node in the same layer. This makes it easy to select *ranges*, since we need
to find the initial value and can then just follow the same-layer pointers.

The values are balanced regarding the nodes, which means "evenly distributed within the layers and nodes".

## Indexes in Django

- `db_index = True`
- `index_together = (('foo', 'bar'), )`
- `ForeignKey` / `OneToOneField`
- `primary_key = True`

## Index(fields, name)

New, fresh from GSoC 2016, arriving in 1.11!

You can define an `indexes` list on a model's `Meta` class. Every element is a field of type `models.Index`.
`models.Index` takes a `fields` list of strings, and a name. But you can also use different index classes, eg special
classes provided by `django.contrib.postgres` to index JSON fields.

## Feature Ideas

- Functional Indexes
- Let `db_index` take other index types, instead of just `True`/`False`
- Define default index types for fields (maybe useful for JSON fields?)
- Refactor `index_together` and `db_index` so that we do not have three ways to define indexes
- Add `GiSTIndex` which allows you to search for locations *near* other locations

Feel free to work on this during sprints!
