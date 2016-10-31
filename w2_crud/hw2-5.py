#!/usr/bin/env python
import pymongo

# It is not necessary to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the students database
db = connection.video
details = db.movieDetails


def find():

    print("find()")

    try:
        cursor = details.find()

    except Exception as e:
        print("Unexpected error:", type(e), e)

    cnt = 0
    for doc in cursor:
        print(doc['countries'])
        if len(doc['countries']) >= 2 and doc['countries'][1] == 'Sweden':
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    find()
