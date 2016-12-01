# Creating documents

* insertOne({"title": "Rocky", "year": "1976"})
* insertMany([{}, {}, {}])
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

* find() — return a cursor, findOne() — return a document

* find().pretty()

* You can use dot notation, but don't forget the double quotes!
	
```
db.<collection>.find( { "tomato.meter": 100 } ).count()
```
* Implicit and operation

```
db.<collection>.find( { rated: "PG" }, { title: 1 } )
```

* Expression matches on Arrays

  * Equality matches on arrays
    * On the entire array
    * Based on any element
    * Based on a specific element
    * More complex matches using operators

```
  # Match on the entire array: The order of the array elements matters
  db.movieDetails.find({ "writers": ["Ethan Coen", "Joel Coen"] }).count()
  
  # Match on any element: No need to put the element in an array format [] in the query
  db.movieDetails.find({ "writers": "Ethan Coen" })
  
  # Match on a specific element
  db.movieDetails.find({ "writers.0": "Ethan Coen" })
  
```

  * Cursors: Look for MongoDB cursor document to know more about it (http://docs.mongodb.org)

```
var c = db.movieDetails.find();
c.objsLeftInBatch();
```

  * Projections: return explicitly include fields. Improve the efficiency of queries by limiting the returned fields.
    * By default, _id field is always returned in the results

# Comparison Operators

* For comparison of different BSON type values, use the comparison operators

  * $eq
  * $gt
  * $gte
  * $lt
  * $lte
  * $ne
