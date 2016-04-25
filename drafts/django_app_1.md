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

### Docker



## Django


## Tests and CI
