Title: DjangoCon Europe 2016 - Day 1 Lightning Talks
Date:   2016-03-31 00:10
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2016 Day 1 Lightning Talks

## Meroku Deployment without git - Markus

 * normally: `git push heroku`, but say you want to deploy a python package
 * possible to build your own heroku slug, but it's hard
 * instead: `npm install -g heroku-slugify`: creates and uploads an appropriate tarball


## Transaction Isolation Levels - Shai

We don't want to talk or think about it, but here they are as defined by the SQL standard:


 - READ UNCOMMITTED: dirty reads may happen
 - READ COMMITTED: non-repeatable reads may happen (default for postgres and oracle)
 - REPEATABLE READ: phantoms may happen (default for mysql, kind of)
 - SERIALIZABLE: none of these happen (only strict implementation in postgres)

MySQL REPEATABLE READ applies only to SELECT, otherwise actions are as if in READ COMMITTED. Therefor Django will change
their MySQL treatment to READ COMMITTED, because it's safer to assume what they might do anyways.

## Mozilla Kinto - Remi

Repeating task of designing an API, implementing a server, deploy it, test it, consume API on client.
Kinto is a JSON storag service, allowing for sync, permission actions, push, encryption, and you can plug Django to use
Django-DB, user-auth and form-validation with a react backend.

## 4 Truths and 1 lie about Australian Animals - Markus

 - Wombats have cubic poop
 - Koala and Wombat pouches are upside down
 - Brown falcons start/spread wildfires as a hunting strategy to make their prey panic
 - sheep manage to roll over cattle-grids
 - Australia has lost a war against ~20k emus

Also, there will be a PyCon AU

## My First ISP Invoice - Peter

 - you can't view the same stuff your customer sees, because you don't have his password
 - emulate view from an admin user 
 - enter: [django-act-as-auth](https://github.com/PaesslerAG/django-act-as-auth)
 - login via admin/username and adminpassword


## Let's All Build A Hat Rack #LABAHR

Basically, read [this](http://hawthornlandings.org/2015/02/13/a-place-to-hang-your-hat/).

Think of something awesome somebody who is not like you, and who has done something, not code (docs, tickets, wiki entries …) and thank them. Bonus points for
public thanks, which might help them as a reference on job search.

`pip install octohatrack` to pool all contributions to a GitHub repo, not just commits.
