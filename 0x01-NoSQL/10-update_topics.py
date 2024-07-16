#!/usr/bin/env python3
"""
    Task 10
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates topics in a collection
    """
    mongo_collection.update_many(
        { 'name': name },
        { '$set': { 'topics': topics } }
    )
