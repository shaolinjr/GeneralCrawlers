from lxml import html
import requests


busch_urls = [
        'https://seaworldparks.com/en/buschgardens-tampa/attractions/rides',
        'https://seaworldparks.com/en/buschgardens-tampa/attractions/shows',
        'https://seaworldparks.com/en/buschgardens-tampa/attractions/exclusive-park-experiences',
        'https://seaworldparks.com/en/buschgardens-tampa/attractions/animal-attractions',
        'https://seaworldparks.com/en/buschgardens-tampa/attractions/other-attractions'
        ]
sea_urls = ['https://seaworldparks.com/en/seaworld-orlando/attractions/kid-size-rides',
            'https://seaworldparks.com/en/seaworld-orlando/attractions/shows',
            'https://seaworldparks.com/en/seaworld-orlando/attractions/rides',
            'https://seaworldparks.com/en/seaworld-orlando/attractions/exhibits']

sea_exceptions = ['https://seaworldparks.com/en/seaworld-orlando/attractions/exclusive-park-experiences']

# for url in busch_urls:

def postMongo(attraction_type, attraction_names, park_name):
    for index, attraction in enumerate(attraction_names):
        type_ = str(attraction_type[0].text_content())
        name_ = str(attraction_names[index].text_content())

        params = {"attraction_name": name_, "park_name": park_name, "attraction_type": type_}
        post = requests.post("http://127.0.0.1:5000/attractions", data=params)
        print(params)

for url in busch_urls:
    page = requests.get(url)
    HTML_tree = html.fromstring(page.content)
    attraction_type = HTML_tree.xpath('//*[@id="aspnetForm"]/div[4]/h1')
    attraction_name = HTML_tree.xpath('//*[@id="aspnetForm"]/div[4]/div[1]/div[2]/div[3]/div/div/div/div/article/h1')

    postMongo(attraction_type, attraction_name, "busch-gardens")


for url in sea_urls:
    page = requests.get(url)
    HTML_tree = html.fromstring(page.content)
    attraction_type = HTML_tree.xpath('//*[@id="aspnetForm"]/div[4]/h1')
    attraction_name = HTML_tree.xpath('//*[@id="aspnetForm"]/div[4]/div[1]/div[2]/div[3]/div/div/div/div/article/h1')

    postMongo(attraction_type, attraction_name, "sea-world")

for url in sea_exceptions:
    page = requests.get(url)
    HTML_tree = html.fromstring(page.content)
    attraction_type = HTML_tree.xpath('//*[@id="aspnetForm"]/div[4]/h1')
    attraction_name = HTML_tree.xpath('//*[@id="aspnetForm"]/div[4]/div[1]/div[2]/div[2]/div/div/div/div/article/h1')

    postMongo(attraction_type, attraction_name,"sea-world")