#!/usr/bin/env python3
"""
    Task 9
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert kwargs as a document
    """
    return mongo_collection.insert(kwargs)
