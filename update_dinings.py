from pymongo import MongoClient
import requests
from lxml import html
from urllib.request import urlopen
from urllib.error import HTTPError
import os
from os.path import join
from clint.textui import progress, puts, colored



sea_urls = ['https://seaworldparks.com/en/seaworld-orlando/dine-and-shop/dining/sit-down-meals',
            'https://seaworldparks.com/en/seaworld-orlando/dine-and-shop/dining/quick-bites']
busch_urls = ['https://seaworldparks.com/en/buschgardens-tampa/dine-and-shop/dining/']

client  = MongoClient()
db      = client.eve
dinings = db.dinings
images  = []

sea_images = []
busch_images = []

#DONE: Verificação de foto já baixada
#DONE: Separação de pastas nas imagens, dinings/<park-name>


def downloadPhoto(folder, photo_url):
    """
        Função que baixa a imagem dado determinada url e pasta
    """
    try:
        u = urlopen(photo_url)
        if not os.path.exists(folder):
            os.makedirs(folder)

        photo = os.path.join(folder, photo_url.split('/')[-1])
        if not os.path.exists(photo):
            localFile = open(photo, "wb")
            localFile.write(u.read())
            localFile.close()
        u.close()
        return photo
    except HTTPError:
        puts(colored.red("HTTP ERROR: 404 - Not Found"))

def get_images (urls,xpath):
    images = []
    for url in urls:

        page = requests.get(url)
        HTML_tree = html.fromstring(page.content)
        images += HTML_tree.xpath(xpath)
    print("URL: %s Found: %d images" % (url, len(images)))
    return images #store in respective list (e.g: sea_images = get_images(...)

def get_downloaded_images (path):
    photos = ["%s/%s" %(path,photo) for photo in os.listdir(path) if os.path.isfile(join(path,photo)) and photo !='.DS_Store']
    return photos

def update_mongo (collection, park_name, images_list, images_path):

    # header console
    puts(colored.cyan("Park name: %s" % park_name,bold=True))
    puts(colored.cyan("Found: %d" % collection.find({"park_name": park_name}).count(),bold=True))
    puts(colored.cyan("Dining images: %d" % len(images_list),bold=True))

    updates = False
    downloaded_images   = get_downloaded_images(images_path) # vai ser vazio na primeira vez que rodar

    for index, dining in enumerate(collection.find({"park_name": park_name})):
        image_url       = images_list[index].attrib['src']
        _images_path    = images_path
        path            = "%s/%s" % (images_path, image_url.split('/')[-1])
        photo           = downloadPhoto(_images_path, image_url)
        name            = dining['dining_name']

        if len(downloaded_images) > 0:

            for image in downloaded_images:
                if photo == image:
                    updates = False
                    break
                else :
                    updates = True
        else:
            updates = True

        # apenas para exibicao no console
        # só exibe e atualiza se tiver alguma foto nova
        if updates:
            params = {"dining_name": name, "dining_image": path}
            puts(colored.green(str(params), bold=True))

            collection.update_one({"dining_name": name}, {"$set": {
                "dining_image": path
            }})
    if not updates:
        puts(colored.blue("********* Nothing new to update here *********"))

#Atualizar collections com a imagem de cada restaurante

# SeaWorld
sea_images = get_images(sea_urls,'//*[@id="aspnetForm"]/div[4]/div[1]/div[2]/table/tbody/tr/td[1]/img')
update_mongo(dinings,"sea-world",sea_images,"images/dinings/sea-world")

# Busch Gardens
busch_images = get_images(busch_urls, '//*[@id="dining"]/article/img')
update_mongo(dinings, "busch-gardens",busch_images, "images/dinings/busch-gardens")

#TODO Magic Kingdom

#TODO Animal Kingdom

#TODO Hollywood Studios

#TODO Universal Studios

#TODO Island of Adventures

#TODO Epcot Center
