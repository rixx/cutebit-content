Title: DjangoCon Europe 2017 - Fighting the Controls
Date:   2017-04-05 01:34
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Fighting the Controls"

**Speaker:** Daniele Procida (Django, django CMS developer)

## Programming vs the world

Programming can be very, very frustrating: receiving different results from doing the same thing over and over again.
This is madness, isn't it?

The story of the Air France Flight 447 shows how we're fighting controls and electronics, and … we don't always win. 
(See also Laurie Anderson's "From the Air"). The failures convey loss of control, and power, and … senseless tragedy,
similar to the flight and fall of Ikarus.

In retrospect, things look differently and much clearer. Aviation calls the confusion in the present confrontation "Loss
of Situational Awareness", which describes a sort of cognitive breakdown, leading to irrational decisions, coming from a
loss of overview.

"Many people think, programming is a science. Not many people, and they are all wrong. Programming is much more like
engineering, or flying. Some people think engineering is a science, and they are wrong too. These things are skills."

We have many analogies: Pair programming is like flying, in that there are two pilots in a cockpit, of whom one is
flying and the other organizing and instructing.

## Programming processes

In nearly all crafts you find a primary and a secondary phase.

The **primary** activity, programming, is sythesising, creative, assembling, moving forward, goal-oriented, imaginative,
getting somewhere, making things happen!

The **secondary** activity, debugging, is analytical, disassembling, moving backwards, problem-oriented, asking how one got
somewhere, asking why things are *not* happening.

Programming is a creative craft. When it comes, failure is unarguable. Trying again is nearly instantaneous and
cost-free. Feedback is nearly instantaneously and cost-free. Debugging is a private affair. (All of these are compared
to other crafts that are not like writing or programming: engineering, or cooking, have much higher respective costs.)

"Debugging is like a miserable relationship. … In debugging we can see a tendency towards cognitive breakdown." It is
predisposed to create a loss of situational awareness similar to the one the pilots experienced. You're starting to feel
anger, and outrage, and confusion, and "Damn it, this can't be happening!"

## Cognitive Breakdown - Loss of Situational Awareness

This is our enemy. This is aviation's enemy aswell, and other than us, they have developed strategies of dealing with
this. They have gathered characteristics:

### Blind Spots

Those are deadly. You can't tell you have them.

### Faulty mental models

When our mental model does not match the representation, we need to break it down and build it back up or recalibrate it
to match observable reality.

### Misjudging cause and effect

Observation and judgement do not always match cause and effect. We need to pull them out of a tight and wrong feedback
loop by making them explicit.

### Poor decision making

Private decision is almost always of poor quality - make decision-making explicit to have correctives here.

## Mitigating loss of situational awareness

- Long detailed **checklists** for normal activities. Very detailed processes for all the emergency procedures and
  debugging parts. We do use checklists for deployments occasionally, seldom for programming, and basically never for
  debugging.
- Communication *needs* to be **explicit** and **verified**. Always communicate and acknowledge communication. It repairs
  our mental model by describing it to ourselves and others and matching it against the judgement of others.
- **STOP**: Don't just do something, sit there! Stop fighting the controls.

We need to talk about this more. There is only so much we can do as individuals. Aciation's approaches are systematic,
cultural, fundamental. Until our debugging mistakes routinely kill us and our customers, this will probably not change.
