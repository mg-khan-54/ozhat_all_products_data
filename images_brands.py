"""This program scrapes the web using lxml and requests.
Scrapping 1st page of the ozhat.com with brand names an images"""

# B/W Controls
# Dansk Ventil Center A/S
# Hjs
# Ledex (brand of Saia Burgess/Johnson Electric)
# Maxtronic Technologies
# TAIYO/TAIYO
# TH-Contact (Saia/Johnson Electric)

import re
from lxml import html
import requests


page = requests.get('https://www.ozhat-turkiye.com/en/search',timeout=10)
tree = html.fromstring(page.content)
brand_item = tree.xpath("//div[@id= 'for_search_result']/descendant::ul[1]/child::div/descendant::"
                        "a[@class = 'catalog-name']/text()")


home_page_links = ['https://www.ozhat-turkiye.com/en/search']
PAGE_LINK = 'https://www.ozhat-turkiye.com/en/search'
COUNTER = 2
for index in range(0,79):
    home_page = requests.get(PAGE_LINK,timeout=10)
    tree_home = html.fromstring(home_page.content)
    COUNTER_STRING = str(COUNTER)
    PATH = "//ul[@class= 'pagination']/descendant::a[text() = '"+COUNTER_STRING+"']"
    all_pages = tree_home.xpath(PATH)
    link = all_pages[0].get('href')
    home_page_links.append(link)
    PAGE_LINK = link
    COUNTER = COUNTER + 1
print(len(home_page_links))
print(home_page_links[-1])

images_source_list = {}
for link in home_page_links:
    page = requests.get(link,timeout=10)
    tree = html.fromstring(page.content)
    image_link = tree.xpath("//img[@width = '200']")
    brand_name = tree.xpath("//a[@class = 'catalog-name']/text()")
    leng = len(image_link)
    for index in range(0, leng):
        source_link = image_link[index].get('src')
        brand = brand_name[index].strip()
        images_source_list[brand] = source_link


COUNTER = 1
for name , link in images_source_list.items():
    if COUNTER <= 477:
        print(len(images_source_list))
        COUNTER = COUNTER + 1
        continue
    clean_name = re.sub(' [ ^ . * / < > ? " : | & $ % { } `]', '', name)
    try:
        with open(clean_name.strip() + '.jpeg','wb') as image_file:
            image_file.write(requests.get(link, timeout=20).content)
        image_file.close()
    except Exception as e:
        print(clean_name)
