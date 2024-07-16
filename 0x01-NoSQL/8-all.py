#!/usr/bin/env python3
"""
    Task 8
"""


def list_all(mongo_collection):
    """
    List documents
    """
    return [document for document in mongo_collection.find()]
