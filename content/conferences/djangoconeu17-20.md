Title: DjangoCon Europe 2017 - Django and the testing pyramid
Date:   2017-04-04 01:20
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Django and the testing pyramid"

**Speaker:** [Aaron Bassett](https://twitter.com/aaronbassett)

## The pyramid

1. The Very Top: Manual testing (most expensive)
2. Functional Testing: End to end testing (long running, expensive)
3. Integration Testing (test that components work well together)
4. The Very Bottom: Unit tests (test **1** thing in isolation, fast and contained)

## BDD: Behaviour Driven Development

Start development from user/usage scenarios. Use something structured to write these scenarios, eg Gerkhin.
Gerkhin uses `Given`, `When` and `Then` as natural language keywords, allows boolean connections with `And` or `Or`, and
variable grouping.

Work on formulating release checklists as well as feature files that describe the behaviours required to be present for a
new release. Do not use those feature files for manual testing (too tedious and much), use checklists for that.

But use something like `pytest-bdd` to work off these files, and look at something like
[splinter](https://splinter.readthedocs.io/en/latest/), that supports testing in multiple browsers. Write BDD methods
for all `Given`, `When` and `Then` statements. (You may also alias a method to other wordings at the same time.)

But these tests run a long time, and long running tests are horrible for coder motivation. And if you avoid making small
changes, your code base starts to smell. This is what unit tests come in. Seeing as they are low-level, we'll need to
mock and patch a lot of stuff. Reuse those mocks and patches! Also mock other services to you, using `httmock` or
`responses`. Think also of mocking failure states.

Integration tests do not need to cover *everything*, because we still have the other three steps of the testing pyramid,
btw. Do not over engineer here!
