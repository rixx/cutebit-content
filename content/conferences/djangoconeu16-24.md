Title: DjangoCon Europe 2016 - Best Practices for Scaling Django
Date:   2016-04-01 00:04
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk Best Practices for Scaling Django

**Speaker:** Anton Pirker is a Django software engineer.

Normal site: Nginx -> Gunicorn -> Postgres, but the site slows down with increased users.

## Debug

1. DjangoToolbar
    - reduce queries
2. Monitor
    - move database to separate server
3. Memcached
    - doesn't increase speed (doesn't work, timestamp debugging)
    - due to cookies
    - don't delete cookies
4. Development machines to get cookies and caching running
5. OperationalErrors
    - maximum connections to postgres
    - enter pgbouncer to re-use connections
6. Long communication
    - async workers: celery + redis
