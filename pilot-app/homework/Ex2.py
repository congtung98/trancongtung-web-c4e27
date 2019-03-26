from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

db = client.c4e

customers_collection = db["customers"]

events = customers_collection.find({'ref':'events'})
ads = customers_collection.find({'ref':'ads'})
wom = customers_collection.find({'ref':'wom'})

def count_customers(ref,ref_name):
    ref_counts = 0
    for i in ref:
        ref_counts += 1
    print('Number of customers group by',ref_name,': ',ref_counts)
    return ref_counts

from matplotlib import pyplot

# 1. Prepare data
customer_counts = [count_customers(events,'events'), count_customers(ads,'ads'), count_customers(wom,'wom')]
# 2. Prepare labels
customer_names = ['Events', 'Ads', 'Word Of Mouth'] 
# 3. Draw pie
pyplot.pie(customer_counts, labels=customer_names, autopct='%.1f%%', shadow=True, explode=[0,0.2,0])
pyplot.title("Events vs Ads vs WoM customers")
pyplot.axis('equal')
# 4. Show
pyplot.show()