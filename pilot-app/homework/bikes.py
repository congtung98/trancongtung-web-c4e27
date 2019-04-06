from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb+srv://admin:admin@cluster0-bvpux.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

bike_app = client.db_bike

Bikes = bike_app["bikes"]
