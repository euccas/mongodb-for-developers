#!/usr/bin/env python
import pymongo

# It is not necessary to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the students database
db = connection.school
students = db.students


def find():

    print("find()")

    #query = {'type': 'homework'}
    #projection = {'student_id': 1, '_id': 0}

    try:
        cursor = students.find().sort('_id', pymongo.ASCENDING)

    except Exception as e:
        print("Unexpected error:", type(e), e)

    for doc in cursor:
        homework_min_score = 1000
        is_min_score = False

        student_score_list = doc['scores']
        print("student score list: {}".format(student_score_list))

        for item in student_score_list:
            if item['type'] == 'homework':
                if item['score'] < homework_min_score:
                    homework_min_score = item['score']
    

        print("student id {} - homework min score: {}".format(doc['_id'], homework_min_score))

        # Loop through student score list again and remove the lowest homework score
        for i, item in enumerate(student_score_list):
            if item['type'] == 'homework' and item['score'] == homework_min_score:
                print("will delete {}".format(student_score_list[i]))
                del (student_score_list[i])

        # Updated the document in database
        print("will update document: scores: {}".format(student_score_list))
        students.update_one({'_id': doc['_id']}, {'$set': {'scores': student_score_list}})


if __name__ == '__main__':
    find()
