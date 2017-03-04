import requests

parks_name = ["magic-kingdom", "epcot", "hollywood-studios", "universal-studios-florida", "animal-kingdom",
              "islands-of-adventure"]

for park in parks_name:

    url = "https://touringplans.com/%s/attractions.json" % park

    response_json = requests.get(url).json()
    for attraction in response_json:
        attraction_name = attraction['name']

        #We need to do a POST to our MongoDB
        params = {"attraction_name":attraction_name, "park_name": park}
        post = requests.post("http://127.0.0.1:5000/attractions", data=params)
        print(params)
