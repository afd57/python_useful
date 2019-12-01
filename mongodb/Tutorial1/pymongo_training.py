"""Pyton Mongo Training.

Training Content:
Connection Mongo DB
Data Modification
Generating Test data
"""

from pymongo import MongoClient
import random
from datetime import datetime


def add_status_field(collection, new_field_name, new_field_value):
    """
    Add new field and value to mongodb collection.

    Args:
        collection: MongoDB collection instance.
        new_field_name: Adding field name
        new_field_value: Adding field value

    Returns:
        The return value. True or False.

    """
    all_items = collection.find()
    status_outcome = ("stopped", "running", "finished")

    for a_record in all_items:
        new_field_value = generating_random_value(status_outcome)
        a_record.update({new_field_name: new_field_value})
        collection.update_one({"_id": a_record.get("_id")}, {"$set": a_record})


def generating_random_value(outcome):
    """
        Return a random value from the outcome set.

        Args:
            outcome possible value set

        Return:
            A value from outcome set.
    """
    size_of_outcome = len(outcome)
    random.seed(datetime.now())
    rand_index = random.randrange(0, size_of_outcome)
    return outcome[rand_index]


if __name__ == '__main__':

    print('Pymong Data Modify Training')
    client = MongoClient('localhost', 27017)
    db = client['lab2']
    collection = db['lesson_group']
    add_status_field(collection, "status", "rand")
