Title: DjangoCon Europe 2016 - To Mock or not to Mock, that is the Question
Date:   2016-03-31 00:07
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "To Mock or not to Mock, that is the Question"


**Speaker:** Ana Balica ([twitter](https://twitter.com/anabalica)) works at Potato London.

Thou shalt write tests! But - how do we write good tests? What do we mock, what don't we mock?

## Mocks vs Stubs

Mocks aren't stubs. Mocks have data and expectations, and they have actual behaviour, while stubs are just
pre-programmed and are made specifically for tests.

## unittest.mock (starting with 3.3)

Mock, MagicMock and patch

## Good Mocks

 * use `with mock.patch.dict('foo.os.environ', {'ENV': 'production'}):` to mock **system envs/calls**
 * use `@mock.patch('sys.stdout', new=StringIO())` to mock **streams/stdin/stdout**
 * use `with mock.patch('foo.requests.get') as mock_get:` for **requests**
 * use `m = mock.mock_opne(read_data='bla'); with mock.patch(foo.open, m, create=True)` to mock **files**
 * use `with mock.patch.object(timezone, 'now',
   return_value=datetime.datetime(2016,1,1,tzinfo=pytz.timezone('Europe/Berlin')))` to mock **timezones**

These mocks save time, make the impossible possible, and exclude external dependencies.


## Combat Bad Mocks

 * Mocks will create methods as you access them, so typos MIGHT NOT BE CAUGHT
 * Use exactly the assert methods you mean
 * assert very specific values
 * or use TDD

Write tests that will last even under changing code, because people will trust positive results, and won't notice false
positives.


## Ways to test

 * functional tests for interaction
 * unit tests for business logic
 * mock in unit tests, but reduce mocks as far as possible for integration tests!
 * mocks can and will provide you with a false sense of security
