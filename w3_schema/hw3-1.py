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

        score_list = doc['scores']
        for item in score_list:
            if item['type'] == 'homework':
                if item['score'] < homework_min_score:
                    homework_min_score = item['score']
    

        print("homework min score: {}".format(homework_min_score))
        print("id: {}".format(doc['_id']))

        updated_score_info = []
        original_score_info = students.find_one({ '_id': doc['_id'] }, {'scores': 1, '_id': 0})
        print("original_score_info: {}".format(original_score_info))
        for i in original_score_info['scores']:
            if i['type'] != 'homework':
                updated_score_info.append(i)

        print("updated_score_info: {}".format(updated_score_info))

        #students.update_one({'_id': minscore_id},
        #                 {'$set': {'score': updated_score_info}})


if __name__ == '__main__':
    find()
