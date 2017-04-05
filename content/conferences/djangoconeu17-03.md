Title: DjangoCon Europe 2017 - Services, Architecture, Channels
Date:   2017-04-03 01:03
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Services, Architecture, Channels"

**Speaker:** Andrew Godwin (Django core developer and developer of Channels)

## The Monolith and Microservices

Django projects by default are monolithic: There is one version of every dependency, it is deployed at once, etc, but
they can lead to spaghetti code and weird dependencies and unclear code paths in growing, large code bases.

Microservices are easier to manage, and can scale independently, provide individual deployment. Dependencies grow more
complex, and bugs are hard to find. They require great communication between teams and services (interpersonal and via
defined APIs). Separation forces some code design.

## Transition to services

* *Identify the cut points*: These might be along app borders or they may not be there at all. This is not trivial at all
and should follow reasonable separation of concerns and reasonable API design.
* *Define APIs between services*
* *Separate datastores and servers*, provides also different levels of security for different datasets.
* *Figure out how to communicate between services*

## Inter service communication

* Direct connections (with or without discovery via an Orchestrator): leads to lots of connections.
* Centralized Routing
* Shared message Bus

Trade-off decisions:

* *Centralized communcation*: great to handle, but single point of failure vs *Distributed communication*: Nasty partly failures.
* *At-least-once delivery*: some messages duplicated vs *At-most-once delivery*: messages may be lost
* *First-In-First-Out*: Backlogs of hell vs *First-In-Last-Out*: Wide ranges of latencies

## Channels

Implementation of a protocol server of ASGI, a message bus and a service worker. Trade-offs (At-most-once delivery,
Low-latency but non-persistent [use celery for that], handles backpressure by errors, leading to short queues, but need
to handle sending errors.)

The channel layer itself is a message bus that you can use for service communication.
The client may send a request on a named channel, receiving then an answer.

## Good practices

* Per-request "correlation IDs": A request ID is passed along even between services. Very useful for tracing something between services.
* Feature Flags: Bundle them in a call's header
* Source of Truth: Let each table be read an written by one service only
* Metrics everywhere: both of performance and network health
* Design for failure
* Don't start with services - start with libraries
