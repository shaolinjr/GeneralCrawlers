import requests
from lxml import html


urls = ['https://seaworldparks.com/en/seaworld-orlando/dine-and-shop/dining/sit-down-meals',
        'https://seaworldparks.com/en/seaworld-orlando/dine-and-shop/dining/quick-bites']


for url in urls:

    page = requests.get(url)
    HTML_tree = html.fromstring(page.content)

    dining_names = HTML_tree.xpath('//*[@id="aspnetForm"]/div[4]/div[1]/div[2]/table/tbody/tr/td[2]/p[1]/strong/span')
    # dining_images = HTML_tree.xpath('//*[@id="aspnetForm"]/div[4]/div[1]/div[2]/table/tbody/tr/td[1]/img')

    for index, dining in enumerate(dining_names):

        name_ = dining_names[index].text_content()
        # image_path = dining_images[index].attrib['src']
        # image_ = requests.get(image_path).content

        params = {"dining_name": name_, "park_name":"sea-world"}
        requests.post("http://127.0.0.1:5000/dinings", data=params)
        print(params)


#
