# Writing your own Django App, Part 0: What is this?

Let's build a website in Django! Woo-hoo!

## Answering ALL the Questions

### Why?

There are a ton of good guides on Django apps out there, most notably the Django tutorial and the Django Girls Tutorial.
I just want to document my way to go about building a Django app. I might learn something, y'all might learn something,
everybody wins.

### What?

A friend of a friend suggested building a Battleship website to get into working with a (different) web framework. I
liked the progression they suggested and decided to do the same in Django.

Details of our requirements are covered in the [MILESTONES.md](link).

### How?

I did the whole thing in a [GitHub repository](https://github.com/rixx/Battleship) that I used to work on this project
and I'll reference commits of that project to document my progress.

## Prerequesites

You should know a programming language and have experience in it. You should know your way around GitHub or even git.
Most importantly, this guide will not explain everything, but it will reference documentation that you should try to
understand.

## Order of Operations

1. Setting up the project
2. Designing a data model
3. Exposing an API
4. Ugly yet simple Client implementation
5. Non-game functionality: Leaderboards, Chats etc
6. Improve UI
7. Do real design work
7. Play with WebSockets, ServiceWorkers etc

