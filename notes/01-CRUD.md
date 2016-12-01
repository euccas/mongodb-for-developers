# Creating documents

* insertOne
* insertMany
* What will happen if one error happens during inserting multiple documents?

# _id Field

* 12-byte hex string
* objectId: Date, Mac address, pid, counter

# Reading documents

* query operators, query string

```
db.<collection>.find( {rated: "PG-13", year: 2009} ).pretty()
db.<collection>.find( {rated: "PG-13"} ).count()
```

* You can use dot notation, but don't forget the double quotes!
	
```
db.<collection>.find( { "tomato.meter": 100 } ).count()
```
	
* Expression matches on Arrays
  * Look for MongoDB cursor document to know more about it
  * Projections: return explicitly include fields. Improve the efficiency of queries by limiting the returned fields.

```
db.<collection>.find( { rated: "PG" }, { title: 1 } )
```

# Comparison Operators

* For comparison of different BSON type values, use the comparison operators

  * $eq
  * $gt
  * $gte
  * $lt
  * $lte
  * $ne

# Find

* find() — return a cursor, findOne() — return a document

