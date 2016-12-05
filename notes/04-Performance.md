# Performance

## Index

In this video, Andrew mentions that while reads are much faster with indexes, writes to a document will happen slower. This is true, but it's worth noting a caveat here: combination operations, such as update and deletion operations, where you find the document you want and then perform a write, will benefit from the index when you're performing the query stage, and then may be slowed by the index when you perform the write. Usually you're still better off having an index, but there are some special cases where this may not be true.

He mentions that indexes in mongodb are in btrees. This is true for MMAP (and therefore for MongoDB prior to 3.0), but it does depend on your storage engine. For example, when you are using WiredTiger, as of MongoDB 3.0, indexes are implemented in b+trees. Again, you can find details in Wikipedia (links provided here for your convenience).

* Index is an ordered list of things
* Index slows down your writes to databases, but your reads will be much faster
* Which optimization will typically have the greatest impact on the performance of a database? - Adding appropriate indexes on large collections so that only a small percentage of queries need to scan the collection.

## Create Indexes

* Use explain to know how fast your query is:


```
db.<collections>.explain().find({<field>: <value>})
```

## Use Indexes

* Indexes are used in find and sort queries
* In sort, indexes can only be used with the defined order

## Compound Indexes

* Compound indexes can be used for multi-key queries, and the query on the prefix key
