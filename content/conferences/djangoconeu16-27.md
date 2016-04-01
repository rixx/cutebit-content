Title: DjangoCon Europe 2016 - Using Django with service workers
Date:   2016-04-01 00:07
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk Using Django with service workers

**Speaker:** Adrian Holovaty ([twitter](https://twitter.com/adrianholovaty)) runs Soundslice.

## Deal with being offline

You can fake offline mode in the chrome dev tools.
Soundslice has an offline mode which can do the same things as the normal page if you pre-download it.

## What is ServiceWorker?

ServiceWorker intercepts every request and response and can choose to forward it, or modify it, or not. If it's a noop,
it just forwards everything.

If requests just go to the ServiceWorker, things work fast, and things work offline.

Capabilities:

 - fetch() API
 - cache (separately from browser cache)
 - arbitrary JS

## Workflow

 - Initial request as normal
 - Initial response, includes registration of Service Worker
 - Request for Service Worker
 - ServiceWorker

Any subsequent request to your domain will go through the ServiceWorker.

```js
if ('servieceworker' in navigator) {
    navigator.serviceWorker.register('/sw.js').then(function(registration));
}
…
self.addEventListener('fetch', function(event) {
    // event.request.url etc.
    event.respondWith(fetch(event.request));
});
```

## Possiblities

 - Cache things (add, retrieve, ...)
 - Preload assets
 - do different actions offline than online
 - Load complete framework (so, routing, templating, controller logic …)
    - ("Run Express server in your browser")

Only in Chrome, Firefox, and Opera. Not: IE, Navigator.

## Replace default offline site

 - **simple:** download and cache a nice offline page in service worker registration, in fetch handler: try download, except NetworkError with fallback
 - **cumulative cache:** cache as soon as users visit a page
 - **UI cache:** make users request content explicitly for offline usage: only save to cache if user requests it

## Problem: We cache too much

 - just cache the navigation etc, but don't cache content unless prompted
 - i.e. save base.html

## App Shell architecture

Download and cache "app shell". In every Cache, immediately return shell.

The shell includes a bit of js, doing an AJAX request with a flag telling Django that it's an appshell request, so
Django can return appropriate content without the shell.

```python
def my_view(request):
    if 'from_appshell' in request.GET:
        base_template = 'empty.html'
    else:
        base_template = 'base.html'
```

## Problem: Cache Invalidation

Solutions:

1. Static assets: Use hashed URLs (css, js, images), and you'll just not have stuff in your cache. (But we still need to
   empty the cache?)
2. App shell: Remember last-updated time and periodically refresh a new app shell
3. App Shell: refresh it on every page load in the background (render old, get new)
4. Data: Give users a way of clearing a Cache

## Problem: Stale Data

E.g. you'll be shown as logged-in.

1. Load the app shell in the background on every page view.
2. Ajax response includes user ID and force reload if mismatched.

Challenge: add ServiceWorker to your website or the DjangoCon's website.

