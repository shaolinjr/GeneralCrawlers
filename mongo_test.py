from pymongo import MongoClient
import requests


# In this example we were able to add the dining list to mongodb using pymongo other then needing the API


#Mongo stuff
client = MongoClient('localhost', 27017)
db = client['new_db']
collection =  db['test']


parks_name = ["magic-kingdom", "epcot", "hollywood-studios", "universal-studios-florida", "animal-kingdom",
              "islands-of-adventure"]

dinings_ids = []

for park in parks_name:

    url = "https://touringplans.com/%s/dining.json" % park

    response_json = requests.get(url).json()

    for attraction in response_json:
        for index,x in enumerate(attraction):
            # print(x)
            dining_name = attraction[index]['name']
            #We need to do a POST to our MongoDB
            params = {"dining_name":dining_name, "park_name": park}

            result = collection.insert_one(params)
            dinings_ids.append(result.inserted_id)




