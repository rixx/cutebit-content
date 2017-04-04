Title: DjangoCon Europe 2017 - Floods List database
Date:   2017-04-04 01:23
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Floods List database"

**Speaker:** Maurizio Latini

## The ECMWF: European Centre for Medium Range Weather Forecasts

Develop core weather forecasts to forecast severe weather, plan high-quality near-surface weather products, climate
monitoring and atmospheric composition forecasting. One of the projects is EFAS: European Flood Awareness System, the
first of its kind in Europe, providing early flood warning up to 10 days in advance to all its partners.
The tasks involves providing a user interface and generate and send alerts if appropriate.
Additionally: Global Flood Awareness System (GloFAS), which is free and operational since 2011.

Flooding accounts for 39% of natural global disasters since 2000, and affected more than 94 million people worldwide.
Current databases have rather sparse coverage of these events. Hence the creation of:

## FloodList

[FloodList](http://floodlist.com) is run by a small team of dedicated people collecting news on flood events around the
world. FloodList doesn't use Django for the heavy lifting, but uses GIS in combination with geoJSON to communicate with
a backend service, then providing lots of useful data to the requesting data.

Future developments include a more normalized structure of the DB, inclusion of the addition of different data sources,
integration of the web interface elsewhere, and creation of a reporting form. It is also planned to use the Common Alert
Protocol to exchange information in the future.
