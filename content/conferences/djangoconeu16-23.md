Title: DjangoCon Europe 2016 - Let's Talk Geo: Adding the "Where" to Your Django Project
Date:   2016-04-01 00:03
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk Let's Talk Geo: Adding the "Where" to Your Django Project

**Speaker:** Corryn Smith ([twitter](https://twitter.com/holacorryn)) is a grad student and used GeoDjango for
Environmental Spatial Analysis.

## What is GIS?

**G**eographic **I**nformation **S**ystems. Includes environmental studies plus the IT side. It deals with creating,
sotring, manipulating, analyzing and displaying spatial data (data of the earth), dealing with different projectsions,
cooridante systems etc.

Everybody uses maps to find places. Use GIS to alyze places: Where to put the next business, where to build a park,
mapping trails, look how the land has changed over a timespan.

GIS visualizes your data, and visualizations are powerful and easily understood!
They can visualize different kinds of data: Points of Interest, Elevation, Physical Features, Routes, Spacial Patterns
to find problems.

## "Where" is important

Show accessibility. Show potential problems (poor areas without stores, when people don't have cars …).

## How can programmers use maps?

 - Display Service Areas: pizza services
 - Points of Interest on a Blog: restaurant list
 - Density maps/Thematic maps: attendees' countries of origin

## Maps with Python and Django

There is `ArcMap` from the ESRI Suite. Automate tasks with `ArcPi`. This is closed-source and expensive.
There is also `qgis`: open source, free, but not popular

There is also `GeoDjango` with an amazing [tutorial](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/tutorial/),
which might be hard to understand.


## Spatial Database

Your database needs the capability to hold geometry data: Postgres and an extension required.

## Geographic Data

Geographic Data contains Points, Lines and Polygons, with these files, that need to be added to the app:
    - .shx (shape index format)
    - .shp (shape format/geometry)
    - .dbf (attribute data)
    - one other

**Sources:**
 - [historical and boundary files](https://www.nhgis.org)
 - [by country and subject](http://www.diva-gis.org/gdata)
 - [land use change over time](http://mrlc.gov)

## Geographic Model

See the tutorial. Models should duplicate the fields in the shapefile, and will be loaded with a `load.py`.

## Django Admin

GIS provides an Admin. Don't use it to edit the data unless you are ready to lose all of it.

## Geo-Friendly API

API is provided via a serializer and json_views.

## Graphics

Use [mapbox](https://mapbox.com) to add a map (like, background) to the project, then call the Data in via your API. Use
leaflet to write css for map appearance.

## Examples
 - [one](https://ungmap.com)
 - [two](https://theyburied.us)
