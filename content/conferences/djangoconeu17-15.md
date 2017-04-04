Title: DjangoCon Europe 2017 - Planet friendly web development with Django
Date:   2017-04-03 01:15
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Planet friendly web development with Django"

**Speaker:** [Chris Adams](https://twitter.com/mrchrisadams)

## Greenhouse effect

The greenhouse effect and global warming are real. People agree that this is bad. CO2 emissions are … well, levelling
off, but not at a nearly high enough rate. We need to work on this.

CO2 emissions come from a large variety of sources, and IT is on the rise: we had about 2% in 2007 - that is about the
same as aviation. It is expected to double to 4% by 2020.

As devs, we don't have control over other industries, but we have direct influence on the usage of datacentres.

## A mental model to think about climate change

### Your servers

Choose renewable energy providers. Many do! (Amazon and Google in Europe, many large companies)

Look at spikes in usage, and use smart provisioning to only use many servers for the spikes and scaling down in between.
So either move to scalable services or even to FaaS/serverless behaviour. This will probably also be financially
lucrative - there are clear financial penalties for bad design.

Django tools for this include `django-configurations`, Clourdfoundry / Heroku, zappa / chalice

### Your Packets

Lossy changes: what do you really need to send? What does the user really want?

Lossless changes: how are things sent? Compression, caching.

Eg 4G is much more energy intensive thant 3G for transmitting data. We're seeing large spikes in WiFi usage aswell. Web
pages are growing increadibly, and transmission is costly in terms of energy.

Django tools for this: CDNs and good nginx config, good middleware, Whitenoise, Webpack 2, Google Closure Compiler,
nginx mod_pagespeed, ImageOptim/Trimage, easy-thumbnails.optimise

### Your Process

Processes are hard - Look into Chris' longer talk about this aswell!

## Resources

- [electrictiymap.org](http://electricitymap.org)
- [CI for your site speed/size](https://speedcurve.com)
- [Website performance calculator](https://performancebudget.io)
- [Life changing essay](https://worrydream.com/climatechange)

There were a lot of links in these slides that I did not type down. You'll have to check Chris' slides for those :( -
it's on slideshare.
