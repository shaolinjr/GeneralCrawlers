import requests


def postMongo(attraction_type, attraction_names, park_name):
    for index, attraction in enumerate(attraction_names):
        type_ = str(attraction_type[0].text_content())
        name_ = str(attraction_names[index].text_content())

        params = {"attraction_name": name_, "park_name": park_name, "attraction_type": type_}
        requests.post("http://127.0.0.1:5000/attractions", data=params)
        print(params)