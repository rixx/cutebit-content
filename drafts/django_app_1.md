# Writing Your Second Django App, Part 1: Setting up the Project

We're starting at the [bare repository](https://github.com/rixx/BattlePony) and end this part with version [v0.1]()

## git: first steps

I started a git repository, made the first four commits, and pushed them to [GitHub](https://github.com/rixx/BattlePony):

```shell
git init
git add README.md
git commit -m '[housekeeping] Initial commit: README.md'
git add MILESTONES.md
git commit -m '[documentation] First version of the milestone definition'
git add CONTRIBUTORS
git commit -m '[housekeeping] Start CONTRIBUTORS list immediately'
git add LICENSE
git commit -m '[housekeeping] MIT license'

git remote add origin git@github.com:rixx/BattlePony.git
git push -u origin master
```

All of these are really important: the `README.md` and the `MILESTONES.md` provide initial documentation for everybody
who just visits this repository. Having a license is pretty much a must for an Open Source project, and naming
contributors of all kinds straight from the beginning is a really good way to go about any project. Have a look at the
[octohatrack](https://github.com/LABHR/octohatrack) project if this sounds interesting or weird to you.

## Isolation

You want isolated development environments for each of your project, so that you can test the dependencies, have
libraries at different versions for different projects and general encapsulation. I went with docker for this project,
but if this seems too much, too steep, too soon for you, you can try using `virtualenv`s (and maybe `virtualenvwrapper` for convenience) instead.

## Django


### Docker

I'm using `docker` and `docker-compose` here. Docker isolates applications and their library from each other and from
the system they are working on (except for the kernel). Docker **containers** are like very very bare Linux operating
systems while **images** contain software and configuration and are loaded into a container. There is a very beginner
friendly [guide](https://docs.docker.com/linux/step_two/) and a more in-depth [architecture
explanation](https://docs.docker.com/engine/understanding-docker/) that you might want to check out.
Docker Compose is a tool to manage applications that need multiple docker containers - we will need at least a container
for our Django application and one container for the database. Docker Compose is also rather [well
documented](https://docs.docker.com/compose/overview/).

The relevant files are the [Dockerfile](link) and the [docker-compose.yml](link), both are reasonably well documented.
Basically, in `Dockerfile` we describe our basic Django image, and with the `docker-compose.yml` we link it to a generic
PostgreSQL image. `docker-compose` is pretty easy to use:

```shell
docker-compose build   # build the containers
docker-compose up -d   # start the containers in the background
docker-compose logs    # see log-output of all containers
```

## Tests and CI
