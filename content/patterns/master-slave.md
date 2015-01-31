Title: The Master/Slave Pattern
Date:   2015-01-21
Category: Patterns
Tags: patterns,basics,master/slave
Slug: master-slave
Authors: rixx
Summary: The common Master/Slave pattern, its habitats and habits. When to use it, when not to.

The Master/Slave pattern is a very common design pattern in software engineering. Interestingly enough, there are two different patterns called Master/Slave, one primarily used in distributed computing, the other mostly found in the field of databases. There are some other uses of the term and discussions on the subject which are explained in the end.

## Master/Slave: Shut Up and Follow

The most popular usa of 'Master/Slave' is in the field of databases. Here descibes a scenario where the slave database(s) replicate everything the master database does, often by reading and replicating all `INSERT`, `DELETE` and `UPDATE` calls in the master database's binlog.

It follows that the master database can recieve both read and write requests while the slave database can only work with read requests. It also should be noted that since the slave replicates both `UPDATE` and `DELETE` commands, a slave database is **not** sufficient as a backup.

## Master/Slave: Divide and Conquer

In distributed computing, the Master/Slave pattern is also referred to as 'Divide and Conquer': the Master has large, repetitive task, so he splits it up and gives it to multiple Slave instances. They do the heavy work and the Master assembles the various returned results.

This is a simple pattern that has a variety of implementations, differing in how a task is split up, whether the master knows about his workers and/or the workers know about their master, if buffering is used to reduce idle times, how the tasks are transmitted etc.

## Master/Slave in History

The term 'Master/Slave' has obvious imperialistic implications. Because of this, various groups interested in Political Correctness, amongst them the L.A. County and the Global Language Monitor have protested the use of these words. Both the [Django](https://github.com/django/django/pull/2694#discussion_r12865261) and the [Drupal](https://www.drupal.org/node/2275877) project subsequently moved to use 'Primary/Replica' instead of 'Master/Slave'.

(Besides, 'Master/Slave' was also used in strange philosophical writings in the 19th century by both Hegel and Nietzsche. Just for the confused student of German literature who stubled upon this page.)


