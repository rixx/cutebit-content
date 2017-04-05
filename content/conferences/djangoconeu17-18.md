Title: DjangoCon Europe 2017 - The OpenHolter project: DIY Cardiometry with Arduino and Django
Date:   2017-04-04 01:18
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "The OpenHolter project: DIY Cardiometry with Arduino and Django"

**Speaker:** [Roberto Rosario](https://twitter.com/siloraptor)

## Electro Cardiometry

Measure the electric activity of your heart. The heart has a variety of mechanical and electrical systems.
Heartbeats have a very typical electrical activity. If you measure it at six vectors, you'll get a complete picture of
the heart works, and then you can add additional measure points at the extremities.

## Holter

Device to measure the electric activity of the heart with three or more electrodes.

EKG is just a snapshot of your heart at a specific time frame, which is not necessarily helpful, so Roberto built his
own Holter (battery driven, so working for longer time frames).

## Open sourcing

Important: cheap, easy, accessible, standard parts. Provide a simple interface and storage. Is open source and uses
open source software and libraries.

There were a lot of challenges involved, especially involving calculations of all kind, and sample rates via magic
interrupts. Heartbeat detection was also nontrivial.

Total cost is about USD 30, and has 12 days battery life (vs 1 day commercially available) and is also otherwise at the
very least up to commercial standards.

Creating an EKG journal vs just an EKG chart is much more valuable.

## App

Also required was an app to extract the data, enrich it with metadata, and present it in a well-structured way. Django
was used to achieve this, allowing to select specific data slices, and attach metadata to it.

Planned improvements are a lot, but the working version is already more than impressive.
