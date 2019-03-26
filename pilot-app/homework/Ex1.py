from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

db = client.c4e

my_post = db["posts"]

my_document = {
    'title': 'Đời là thế thôi',
    'author': 'AmTiDiaPhu',
    'content': 'C4E27. Lớp học của những thằng nghiện cờ nhân phẩm. Mỗi tối đi học về là lại đánh dăm ba ván. ',
}

my_post.insert_one(my_document)
