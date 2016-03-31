Title: DjangoCon Europe 2016 - What is ReactJS?
Date:   2016-03-31
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "What is ReactJS"


**Speaker:** Tomáš Ehrlich ([twitter](https://twitter.com/tomas_ehrlich)) initiated PyCon CZ and is a translation
manager for Django Girls

## ReactJS

React is a library, not a framework, for user interfaces, and thus is basically the view/frontend/presentation
logic/template engine, it renders data and handles events.
React's main feature is only rendering diffs on changes, not re-rendering the entire DOM, because DOM operations are
expensive.

## React with Django

You could just use React in Django as a frontend library, and integrate it with existing projects, but it's not DRY,
you'd re-write lots of stuff.

Instead you could use full-stack react (server-side), replacing views and templates, and use Django only to provide
Business Logic, Authentication, Form Validation and Admin Functionality via REST APIs.
