Title: Ligretto
Date:   2016-11-02 11:01
Category: general
Tags: data,d3,ligretto,games
Lang: en
Authors: rixx
Status: draft
Summary: I played Ligretto with some friends and you won't believe what happened next.

## The Setting

Because my friends are the most enduring people there are, they indulged me
and played several hours of [Ligretto](https://en.wikipedia.org/wiki/Ligretto) with me
on my birthday. Yay! We had decided early on that we would play until somebody reached
a total score of either 100 or -100 points.

Because my friends are nerds, as the hours passed we noticed that we were generating the
most interesting data, and we'd have to look at it later on.

## The Score

Let's look at the simple and total scores over the course of the game first: 

<div id="fig_scores"></div>

In the beginning, we all kind of had to find our footing - Bashful, Sleepy and Dopey were new
to the game, while Doc plays regularly and the others had at least tried it once before.

## The Handicap

Doc or Happy might have won awfully soon if we hadn't played with a handicapping mechanism:
Taking the worst score as a baseline, all others were assigned a handicap (an additional
card they had to get rid off) score for every ~10 points they were ahead of the lowest score.
You can see it kicking in beautifully, first for Happy then for Doc, in the middle of the game.

<div id="fig_handicap"></div>

## The End

While the scores began to rise again when we were closer to each other and the handicaps shrunk,
exhaustion set in for many of us when Dopey suddenly hit his stride, took off, and ended the game
(which, to be honest, most of the players were grateful for).

<div id="fig_avg"></div>

The higher scores towards the end of the game were probably both due to exhaustion and
grown proficiency at the game - longer games yield higher scores, and nobody managed to end
a game. Looking at the whole game, our average score remained remarkably stable.

## Learnings

 - While Doc ranked first or second for most of the game, he rarely finished with the most
   points - instead, he consistently scored positive amounts, even when his handicap was huge.
 - Next time, we're going to mark who ended a round, because it's not always the person with
   the most points
 - Graphing things can be fun and easy - for these graphs, I played with 
   [mpld3](http://mpld3.github.io/) which compiles [matplotlib](http://matplotlib.org/) plots
   to [d3.js](https://d3js.org/) svgs.
 - Everybody should play more Ligretto!
