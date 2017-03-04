import requests

parks_name = ["magic-kingdom", "epcot", "hollywood-studios", "universal-studios-florida", "animal-kingdom",
              "islands-of-adventure"]

for park in parks_name:

    url = "https://touringplans.com/%s/dining.json" % park

    response_json = requests.get(url).json()
    for attraction in response_json:
        for index,x in enumerate(attraction):
            # print(x)
            dining_name = attraction[index]['name']
            #We need to do a POST to our MongoDB
            params = {"dining_name":dining_name, "park_name": park}
            post = requests.post("http://127.0.0.1:5000/dinings", data=params)
            print(params)
