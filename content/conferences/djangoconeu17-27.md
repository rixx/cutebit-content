Title: DjangoCon Europe 2017 - Weird and Wonderful things to do with the ORM
Date:   2017-04-05 01:27
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Weird and Wonderful things to do with the ORM"

**Speaker:** Marc Tamlyn (Django core dev)

**The ORM is weird because databases are weird. With the ORM you do not need to write SQL.**

We need to define a real world style examples because projects in examples tend to be too naive to demonstrate SQL/ORM
features. There is still a lot of deliberate naivety in the examples here, too.

Let's say we have a `Department`, `Employee`, `Customer`, `NewVehicle`, `UsedVehicle`, `OwnedVehicle` (no `Vehicle` due
to expensive JOINs), also `Task`s.

## Querying your data

Registration plates can be found by year in the UK with regexes such as `\w\w17\w\w\w` and `\w\w67\w\w\w` for 2017.
We want a nice API for this, such as (`plate__year=2017`). This can be implemented via a custom `Lookup`, defining a
Lookup with the name `year`, and an `as_sql` method, returning a SQL string filtering for a regex plus a list of
arguments (the original list twice, due to compiler magic). We then can register the lookup on the `CharField`.
You can add lots of fancy validation logic here, aswell.

But since plate patterns have changed too much, we really want to `.order_by(PlateYear(…))`. We could implement this
with a very very long `Case`-`When` chaining, implementing that `year` logic in an annotation, then ordering by it.
Put this in a function (`def PlayteYear(field): return Case(…)`), and boom! you're done.

## Encapsulating your logic

A used vehicle may be sold in cash, or via credit card, and exchanges may happen, and you want credit checks and …
utility functions will pile up, even if most of it is not actually used, and checks for transaction types, and lots of
error handling. Having all those methods on the `vehicle` object makes things unclean. We actually want just to access a
transaction field on the vehicle and have that know which methods are relevant to it.

We're going to have a custom field storing the transaction type, and when accessing it
The `BaseTransaction` class takes a vehicle, and its subclasses may implement different versions of the required
transaction methods (eg `complete_transaction`), and also a slug attribute.

`TransactionTypeField(CharField)` will return the slug in `get_prep_value`, and return a `TransactionDescriptor(value)`
in `from_db_value`. `TransactionDescriptor` provides a `__get__` method which may be used to instantiate the transaction
via the provided slug value and a mapping somewhere. Assigning values to `.transaction` needs to be implemented via
`TransactionDescriptor.__set__`.

You won't need this level of complexity at first. But later on you can encapsulate several complex processes applicable
to instances of the same model depending on its age/size/price/payment process with a common interface that is easily
accessible. This provides also very testable code.

## Advanced prefetching

We want reports! What has happened to all cars in for service today, and: what have the mechanics done today?
We'll have a lot of `Task` objects, connecting an employee, a vehicle, an action, notes, and timestamps. The vehicle is
*not* done via a `GenericForeignKey` (which is complex, and may lead to weird errors), instead it's going to be a
`RegistrationPlateField` (just go with it).

### See all employees of the day with tasks

`department.employee_set.prefetch_related(PrefetcUserTasks(today_only=True))`: This needs a wrapper on top of the
prefetch object. We customize the queryset in `PrefetchUserTasks(Prefetch).__init__(self, today_only=False)`. This
super()s the init call: `super().__init_('prefetched_tasks', qs, 'task_set')` with a custom QuerySet. This then sets
`employee.prefetched_tasks` on the returned objects.

### See all vehicles of the day

We'll use a manager: `RelatedTaskManager(Manager)`, instantiating it properly. In `get_queryset` we then query for the
license plate. We use a `TasksDescriptor(ReverseManyToOneDescriptor)`, specifying `related_manager_cls =
RelatedTaskManager`, and `pass` in the `__init__` method to avoid dark magic. And we need to set the `TaskDescriptor` on
the `Vehicle` class.

Additionally add a `RelatedTaskManager.get_prefetch_queryset(self, instances, queryset)`: we build a list of plates on
the instances already loaded from the database, and then modify the queryset by filtering it by the plates already
found. We then return a 5-tuple of:

```python
return (
   queryset, # The new queryset of tasks we just built
   lambda result: result.registration_plate  # yield the queried attribute
   lambda inst: inst.registration_plate,  # yield the attribute that is attached to this
   False,  # Many objects, please
   'task_set' # cache name
)
```

So we can do `UsedVehicle.objects.prefetch_related('task_set')`.
Just to add a nice API we are going to add a custom `Prefetch` object again and can then: filter vehicles by the day of
the task.

### Wrapping up

Beautiful APIs are possible.

Expressions and lookups are powerful tools to write clean, concise APIs.

Descriptors are magical and hard to debug.

Prefetching can apply to any way you can connect the two objects together. They do not need any prior relation.

### The future!

- We've finally got `SubQuery`!
- We've got functional indexes
- TBD: Virtual fields resolving to an expression
- TBD: Lazily evaluated prefetching across multiple querysets
