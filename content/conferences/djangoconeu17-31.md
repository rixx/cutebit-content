Title: DjangoCon Europe 2017 - Docker Lessons from Real-World Projects
Date:   2017-04-05 01:31
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Docker Lessons from Real-World Projects"

**Speaker:** Rivo Laks

## The Problem

- Hosting dozens of projects
- Single server runs multiple projects
- Projects started to interfere with each other

## The solution

- Good isolation out of the box
- Lots of tutorial online, but little practical experience with bigger projects

## Docker

- Isolation
- Use images (basically static executables) to start containers (like processes) which are completely isolated from each
  other, accessing volumes to share data

## Implementation

Build for Django, node, database, other services, and build for production first.

For Django: Use the official `python` image, then install dependencies, add source code, and use volumes for data directories for
assets, media and logs. The node container, on contrast, is only run once on deploy time to bundle css and js using
webpack. Other services were mostly built using official images with little modification except for the use of volumes
for data. All services communicate via network.

Docker Compose is a tool for defining and running multi-container Docker applications, helping to define and control
multiple containers at once. It also makes networking much easier. It involves one configuration file and a small set of
easy commands.

Deployment builds the containers (`docker-compose build`), and runs the node build command, collect static files, run
migrations, and start the containers (`docker-compose up`).

Development does some things differently: Sources are not baked into images, postgres and other services are run
locally, and all this is tied together via a different Docker Compose config. Source code is mounted as a volume,
runserver is used instead of gunicorn (as well as webpack watch mode), and Dockerfiles differ slightly, too. Postgres is
run locally, with project specific volumes for data.

## Quirks

Introduce makefiles to shorten the loooong commands `docker-compose run --rm django ./manage.py migrate`. While you are
at it, add a `make setup` executing all the initial steps.

Service discovery: Nginx uses Docker's built-in routing, which fails when containers are restarted (with new addresses)
due to nginx only looking up addresses once. Fixed by a service monitoring docker events and reloading nginx when
needed.

Services need to be booted in order (Django after Postgres). There is a lot of `wait-for-it` scripts for this.

Filesystem performance may suffer on non-Linux OS, aswell as some other weird bugs due to Docker running inside a VM.

PyCharm supports Python inside Docker well, but there are still bugs, eg the inability to recognize newly installed
packages, and running an app inside PyCarm is also tricky then.

Most commands need to be run with docker, which requires changes in a lot of dependent service scripts.

## Should you use docker?

There is definitely a steep learning curve, that does not level off too soon. You will run into very new issues. There
is not the greatest tooling available, and you'll have performance problems outside of Linux.

But: you get dependency isolation, you have reproducability. Makes new services easily addable. Limiting and monitoring
resource usage is easier. Having a single-step project setup is also quite cool.

Migrating is hard, but starting with it might make sense. Check also Thorgate's open source project
[template](https://github.com/thorgate/django-project-template).

Consider carefully if you can spend a New Tech Point on docker? Because per-project you can only spend so many time and
effort on new and unexplored technology.
