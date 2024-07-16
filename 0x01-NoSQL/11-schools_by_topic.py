#!/usr/bin/env python3
"""
    Task 11
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of topics
    """
    return list(mongo_collection.find({ "topics": topic }))
