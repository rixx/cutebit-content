Title: DjangoCon Europe 2016 - HTTP/2: Why Upgrading the Web?
Date:   2016-03-31 01:07
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 talk "HTTP/2: Why Upgrading the Web?"

**Speaker:** Quentin Adam ([twitter](https://twitter.com/waxzce)) is the CEO of Clever Cloud.

## HTTP

HTTP is an old protocol and everybody likes, knows and runs it, it's entirely based on request/response patterns. It has
the four concepts of a verb (`GET`, `POST`, etc), a resource (url), headers and a body. It is heavily extendable as
demonstrated by WebDAV.

It has, by now, several downsides: 
 - the transfer size/overhead is huge
 - pipelining: We wait for responses before sending new requests which isn't great for performance
 - cookies are always re-sent

There are many hacks that have become best practices, trying to work around HTTP:
 - use asset domains to avoid sending fat cookies over and over
 - use multiple domain names to parallel downloads and enhance performance
 - bidirectional data stream hacks such as websockets

## HTTP/2 draft

The draft is by the IETF HTTPbis working group.

 - binary protocol
    - hard to read, but encrypted compressed HTTP isn't readable either, and wireshark supports HTTP/2
    - safer
    - concise
 - build only one TCP connection to utilize streams
    - no overhead, just frames
    - within streams you can prioritize which content you push first
    - push resources to cache, too, for better UX
    - *side note by me:* isn't that kind of a security risk?
 - headers will be compressed (HPACK) and persisted, for less repetition
 - the four concepts remain
 - side note: benchmarks say that HTTP/2 is faster in most modern browsers

## Update process

 - negotiate protocol with 101 switching
    - already in use for websockets
    - but slow, requires two connections
 - join TLS and HTTP protocol negotiations: NPN + ALPN

## ToDo

 - changes in frameworks are required: Django is not ready for HTTP/2
 - great opportunity for committers!
 - play around with the python package `hyper` (by [@lukasaoz](https://twitter.com/lukasaoz))
 - go [here](http://http2.github.io) for specs and implementations
 - install wireshark and play
