Title: DjangoCon Europe 2017 - Using type checking in Django projects with mypy
Date:   2017-04-04 01:24
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Using type checking in Django projects with mypy"

**Speaker:** Daniel Moisset (mypy contributor)

## Static typing

Static typing is really hard. People tend to have used bad statically typed languages, or have used statically typed
languages badly, and this results in not liking static typing as a result. But Python is different.

Type can mean three things: either the structure or memory layout for an object on runtime, or a label over some piece
of source denoting an object, or sometimes a name for an interface of several objects.

Static typing is not the same as explicit typing: you need not expose the type of everything.
Static typing is not necessarily required to run the program.
Static typing does not have to be mandatory in the whole code base.

## MyPy

MyPy is a static type-checker for Python. After you have added type annotations (in some places, others can be
inferred), you run mypy and get warnings on type mismatches. MyPy requires Python3 to run, but can run on a Python2 code
base, too!

MyPy is mostly useful at development time, because Python is "lazy" about reporting obvious type errors, and some type
errors are not all that obvious. Since you surely have good tests, the use of MyPy will probably extend primarily to dev
time. Neither performance nor bug-catching is the explicit goal of the project. Instead it strives to use types more as
representation and less as "only metadata".

It also helps in term of readability. Annotations specify author intent - they are like a docstring, but (due to mypy)
without the code rot, or like a very very compact doctest. They are also very useful when refactoring or understanding
new code bases or legacy code. ([See also](https://www.machinalis.com/blog/a-day-with-mypy-part-1/))

It is also wonderful for tool integration, improving completions, assisted refactoring, or documentation generators.

The introduction of mypy can be gradual, and does not need to be complete - you can mix and match, and leave out parts
where type annotations just do not make sense. The type checker is completely separate and does not mingle with run-time
semantics.

There are also typesheds/.pyi "stubs". This is a normal Python file (i.e., it can be interpreted by Python 3), except
all the methods are empty. Python function annotations (PEP 3107) are used to describe the types the function has.

## Django

Django type hints are WIP: request and response, generic views, url resolver are done, other things are coming up. They
are easy to use, and read, so go ahead and use them!

### Possible problems

- Too dynamic code is not really suitable
- Duck typing has some ad-hoc support, fixes are planned
- If you depend on an unsupported library, you may use it, but annotations may be inconsistent and you may have to
  update things later. ([See also](https://www.machinalis.com/blog/a-day-with-mypy-part-1/))
