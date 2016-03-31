Title: DjangoCon Europe 2016 - Django for IoT: From Hackathon to Production
Date:   2016-03-31 01:01
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "Django for IoT"

**Speaker:** Anna Schneider ([twitter](https://github.com/windupanna)) has a PhD in biophysics and learned Django at the
Hackathon where whe started WattTime. See also http://unconsciousbiasproject.org.

## IoT

Internet of Things is meant when something that is not typically a computer transmits data and maybe even responds to
control. IoT can involve embedded programming, but many things just have usable APIs.

## Patterns

 - Use `db_index` early and on timestamps, because you will have loads of data.
 - use tasks instead of views
    - tasks initiate actions
    - tasks may monitor (pull attributes and statuses)
    - tasks may control (set attributes and statuses)
 - since tasks run async, pass pks and not objects
 - encapsulate the client/vendor library so that you can swap out devices
 - break up into apps for production
    - **devices**: Device models, later maybe views for devices.
    - **observations**: Data models, later analytics views.
    - **interactions**: tasks.py, later on administration
    - **vendor**: wrapper for client libraries
 - use celery for async tasks
    - don't use RabbitMQ to persist things, redis may work
 - use the [cookiecutter](https://github.com/aschn/cookieutter-django-iot)

IoT can actually improve the world, so go out there and try it.
