#!/usr/bin/env python
import pymongo

# It is not necessary to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the students database
db = connection.students
grades = db.grades


def find():

    print("find()")

    query = {'score': {'$gte': 65}}
    projection = {'student_id': 1, '_id': 0}

    try:
        cursor = grades.find(query, projection).sort('score', pymongo.ASCENDING).limit(1)

    except Exception as e:
        print("Unexpected error:", type(e), e)

    for doc in cursor:
        print(doc)


if __name__ == '__main__':
    find()
