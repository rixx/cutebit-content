Title: DjangoCon Europe 2017 - Understanding the amazing world behind your ORM
Date:   2017-04-04 01:21
Category: conferences
Tags: conferences,protocols,talks,python,django
Lang: en
Authors: rixx
Summary: Summary of the DjangoCon Europe 2017 talk "Understanding the amazing world behind your ORM"

**Speaker:** [Louise Grandjonc](https://twitter.com/louisemeta)

This talk details how to find what results in slow endpoint times:


## How do we end up with performance problems?

The ORM executes queries that you might not expect, and its queries may not be optimized, and you won't know it.

## How can we catch the problems without having to guess?

There are various tools:

1. Django debug toolbar … helps you to see queries, but doesn't show you production times.
2. Django devserver: can log all of your queries.
3. **Look at your database logs!** This gives you actual data, and can be repeated in production.

```shell
psql -U user -d databasename
# show log_directory;
# show data_directory;
# show log_filename;
```

Now you just need to connect the query from the log with the code executing it. This is made a bit harder by the fact
that query execution is lazy, so the query is not exactly executed when it is composed. Follow the flow of the connected
model - where is it filtered? Where are the resulting objects used? Are they passed to somewhere else, e.g. templates?

Be wary of loops. Use `select_related` (JOIN) and/or `prefetch_related` (separate queries), as appropriate.

## Use the queryplanner

Take a slow query, and put it into `EXPLAIN ANALYZE`, which tells you what the queryplanner is doing and outputting.
It tells you:

- The cost of retrieving the first row
- The cost of retrieving all rows
- The number of rows returned
- The average width of a row
- The number of times the query needs to be executed (when using `ANALYZE`)

… and then be careful when and where you're creating your index - take care what kind of scans happen: Full table scans,
Index Scans, Bitmap Heap Scan …

And then also look into `JOIN`s (eg. Merge Join used for big tables, with indexes practical to avoid sorting).

Finally, `ORDER BY`: Look at when the sorting happens, since it happens in memory, and different sorting mechanisms use
different amounts of memory (in-mem vs not).

## What does it change in our everyday developer job?

- Looking at your DB logs can help you build a website with good performance
- Tells you where your queries come from
- Be careful about loops! Use `prefetch_related` and `select_related`
- If you have a slow query, use `EXPLAIN`
