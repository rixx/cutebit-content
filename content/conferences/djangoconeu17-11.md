Title: DjangoCon Europe 2017 - Serverlessness - augmenting your Django apps with Functions-as-a-Service
Date:   2017-04-03 01:11
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Serverlessness - augmenting your Django apps with Functions-as-a-Service"

**Speaker:** [Tom Dyson](https://twitter.com/tomd) (Wagtail)

## The Problem

There are loads of use cases for very small one-feature websites that just expose one simple function to people.
(E.g. some special lookups in publicly available data, reformatting of data, etc).

These simple tools are often written at once, then deployed for a while, then sink into lack of maintenance and are
finally taken off.

The fun part is having an idea and writing it. The less fun part is installing an OS, installing your servers, tools,
configuring them, making them play with each other, set up DNS, SSL, firewall, backups, and monitoring, and Launch
(which is fun again …).

## "Serverless" (aka Functions as a Service?)

First off: this is a misnomer. There are still servers behind everything.

All of these platforms have some command line deploy tool, and suddenly your script is available on the internet.
Abstraction from containers in the cloud (from VMs in the cloud (from dedicated servers (from owned servers))).

You can now have easy auto scaling (up aswell as down) and parallelisation. You can trigger functions with more than
just HTTP requests - most platforms interface with logs, s3 uploads, pub/sub, email, and cron.

Serverless platforms encourage better design: "Small pieces, loosely joined" and "write less code".

## Toolkits

- AWS Lmabda
- Goole Cloud Functions
- Azure Functions
- Serverless Framework (\o/)
- Chalice (least magic)
- Zappa
- [now](https://zeit.co/now) ("like heroku for hipsters")

## Common use cases

- Thumbnailing
- Document processing
- Augmenting static sites
- Mobile & JS apps
- Creating APIs
- Bots

## Exemplary usage

```shell
pip install chalice
chalice new-project test
vim main.py
chalice local  # debugging
chalice deploy
```

## Serverless Django

- Shrink your project
- Flatten the bumps (by extracting less than performant stuff to FaaS)
- Move cautiously to microservices
- Consider JAMStack for CMS projects
- Handle more varied events

## Caveat

- Startup times (not below 5 minutes)
- Platforms are not quite mature
- No cost cap
- No persistance
