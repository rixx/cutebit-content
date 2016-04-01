Title: DjangoCon Europe 2016 - Don't be afraid of writing migrations
Date:   2016-04-01 00:05
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk Don't be afraid of writing migrations

**Speaker:** Markus Holtermann ([twitter](https://twitter.com/m_holtermann)) is a Django core developer with focus on
the migrations framework.

Some things, `makemigrations` cannot do, and that's where you come in. Everything here is in in Postgres, should work in
MySQL, SQLite unsure, Oracle … ask your support.

## General
```python
from django.db import migrations

class Migration(migrations.Migration)
    dependencies = []
    operations = []

```
 - `dependencies`: other migrations that you depend on
 - `operations`: all required operations
 - migrations are run in correct order when applied and reverse order when unapplied

## Recipe 1: Optimizing makemigrations output

Output is not always ordered cleverly, so that fields will be added in the very end, so you might want to change the operations around.
Models are also processed in alphabetical order. (You could submit a patch here.)

## Recipe 2: Adding a non-nullable column

First have a class with an initial data migration: `forwards` and `backwards` methods for generating and deleting two
data points. Then, after migrating, you want to add another column which is nullable. *Then* just define a forwards
method.

```python
def forwards():
    for author in Authors.objects.all():
        # fill data


class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop)
    ]
```

*Then* we make the column non-nullable, and tell Django that we know what we are doing.


## Recipe 3: Rename an App Without Dependencies

You must not have any *incoming* foreign keys which depend on this app.

To the model class, add this and migrate.
```python
    class Meta:
        db_table = 'rename_app_here'
```

Then run `migrate rename_app zero --fake` to make Django think that you have not applied any migrations yet.

Then change the app name everywhere (`settings.py` etc.). Then fake-migrate back to the very front and delete the Meta
attribute, and migrate.


## Resources

We will get a GitHub repository with examples, check Markus' [GitHub](https://github.com/MarkusH) later.
