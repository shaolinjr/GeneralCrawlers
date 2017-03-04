import requests
from lxml import html


urls = ['https://seaworldparks.com/en/buschgardens-tampa/dine-and-shop/dining/']


for url in urls:

    page = requests.get(url)
    HTML_tree = html.fromstring(page.content)

    dining_names = HTML_tree.xpath('//*[@id="dining"]/article/div/h1')

    for index, dining in enumerate(dining_names):

        name_ = str(dining_names[index].text_content())

        params = {"dining_name": name_, "park_name":"busch-gardens"}
        requests.post("http://127.0.0.1:5000/dinings", data=params)
        print(params)

