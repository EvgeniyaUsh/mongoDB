from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)
account_collection = client.test_database.Account

pipeline = [{"$unwind": "$sessions"},
            {"$unwind": "$sessions.actions"},
            {"$group": {"_id": {"number": "$number", "types": "$sessions.actions.type"},
                        "lasts": {"$push": "$sessions.actions.created_at"},
                        "count": {"$sum": 1}}},
            {"$group": {"_id": {"number": "$_id.number"},
                        "actions": {"$push": {"type": "$_id.types", "last": {"$max": "$lasts"}, "count": "$count"}}}},
            {"$project": {"number": "$_id.number", "_id": 0, "actions": 1}}]

pprint(list(account_collection.aggregate(pipeline)))
