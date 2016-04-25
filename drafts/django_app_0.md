# Writing Your Second Django App, Part 0: What Is This?

Let's build a website in Django! Woo-hoo!

## Answering ALL the Questions

### Why?

There are a ton of good guides on Django apps out there, most notably the Django tutorial and the Django Girls Tutorial.
But those are beginner level tutorials - I want to show my way of building a Django application with some more advanced
features - we will talk about docker, Django Rest Framework, channels and py.test here! (No async and task queues here,
leave that for your third Django app.)

### What?

A friend of a friend suggested building a Battleship website to get into working with a (different) web framework. I
liked the progression they suggested and decided to do the same in Django.

Details of our requirements are covered in the
[MILESTONES.md](https://github.com/rixx/BattlePony/blob/master/MILESTONES.md).

### How?

I did the whole thing in a [GitHub repository](https://github.com/rixx/BattlePony) that I used to work on this project
and I'll reference tags of that project to document my progress.

## Prerequesites

You should know a programming language and have experience in it. You should know your way around GitHub or even git.
Most importantly, this guide will not explain everything, but it will reference documentation that you should try to
understand.

## Order of Operations

Links to the corresponding Blog Posts will follow as soon as those are up.

1. Setting up the project
2. Designing a data model
3. Introducing users and permissions
4. Exposing an API
5. Ugly yet simple Client implementation
6. Non-game functionality: Leaderboards, Chats etc
7. Improve UI
8. Do real design work
9. Play with WebSockets, ServiceWorkers etc
