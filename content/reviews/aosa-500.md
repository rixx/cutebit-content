Title: AOSA4 - 500 lines or less
Date:   2016-07-16 01:00
Category: reviews
Tags: reviews,books,aosa
Lang: en
Authors: rixx
Status: draft
Summary: Review of the latest AOSA book "500 lines or less"

This is my review and summary of the latest [AOSA](http://aosabook.org/en/index.html) book "500 Lines or Less", where
experienced programmers solve interesting problems in short(-ish) programs. The book is available for free online, but
if you are interested and can afford it, please consider [buying](http://aosabook.org/en/buy.html#fh) the PDF or
paperback versions.

## [Blockcode: A visual programming toolkit](http://aosabook.org/en/500L/blockcode-a-visual-programming-toolkit.html)

[Dethe Elza](https://twitter.com/dethe) introduces us to a minimal version of [Waterbear](http://waterbearlang.com/).
Waterbear wraps existing language with a block-based syntax. (Block-based languages are visual programming languages
like [Scratch](http://aosabook.org/en/500L/blockcode-a-visual-programming-toolkit.html) and [Lego
Mindstorms](http://aosabook.org/en/500L/blockcode-a-visual-programming-toolkit.html).)

Since Waterbear is browser-based, we are shown well-structured, understandable JavaScript code, as far as I can tell - I
don't use JavaScript normally, and I enjoyed reading the code shown here, especially since it does not rely on
external libraries such as jQuery, and includes comments and necessary clean-up routines.

In addition to the Code introduced, I want to highlight the excellent "Lessons Learned" section in the end of the
chapter. First, we get a very concise take on the MVC pattern in modern browser application. Dethe then reflects on the
advantages of being forced to reduce a larger project to 500 LOC or less:

 - a small prototype helps you realize what core features of your project are, and what features are not important or
   even historical and should be removed
 - a small prototype helps you experience at very small costs/penalties for failure
 - a small prototype makes it more apparent what features should be introduced next

