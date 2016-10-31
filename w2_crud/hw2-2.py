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

    query = {'type': 'homework'}

    try:
        cursor = grades.find(query).sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])

    except Exception as e:
        print("Unexpected error:", type(e), e)

    id = -1
    # for doc in cursor:
    #     if doc['student_id'] != id:
    #         print("delete doc _id {}".format(doc['_id']))
    #         grades.delete_one({'_id': doc['_id']})
    #         id = doc['student_id']

    for doc in cursor:
        print(doc)


if __name__ == '__main__':
    find()
