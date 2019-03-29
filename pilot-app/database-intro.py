from pymongo import MongoClient
from bson.objectid import ObjectId

# 1. Connect mongodb
mongo_uri = "mongodb+srv://admin:admin@cluster0-bvpux.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# 2. Get / Create database
db_demo = client.test_database

# 3. Get / Create collection
first_collection = db_demo["my_collection"]

# 4. Create document
# game_document = {
#     "title": "FO4",
#     "description": "Football game",
# }

# 5. Insert document
# first_collection.insert_one(game_document)

# 6. READ
# 6.1 READ all
# all_documents = first_collection.find()
# for document in all_documents:
#     print(document["title"])

# 6.2 READ one
# one_document = first_collection.find_one({"title": "LoL"})
# print(one_document)

# 7. DELETE
# delete_document = first_collection.find_one({"_id": ObjectId("5c979c26c6c5843f246d1889")})

# if delete_document is not None:
#     first_collection.delete_one(delete_document)
#     print("Delete Complete!")
# else:
#     print("Not Found")

# 8. UPDATE
update_document = first_collection.find_one({"_id": ObjectId("5c979c3fc6c58431988fea7b")})
new_value = { 
                "$set" : { 
                            "title": "Khong biet", 
                         } 
            }
first_collection.update_one(update_document, new_value)




