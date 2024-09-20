"""This program extracts data from Ozhat.com including all brand products."""
import csv
from lxml import html
import requests

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

all_brand_links = {}
LENGTH_HOME = len(home_page_links)
PAGE_NUMBER = 1
for links in home_page_links:
    brand_links = requests.get(links,timeout=10)
    tree_brands = html.fromstring(brand_links.content)
    brands_link = tree_brands.xpath("//a[@class= 'catalog-name']")
    brands_names = tree_brands.xpath("//a[@class= 'catalog-name']/text()")
    length = len(brands_names)
    for index in range(0,length):
        brand_name = brands_names[index].strip()
        brand_link = brands_link[index].get('href')
        all_brand_links[brand_name] = brand_link
LENGTH_BRAND_LINKS = len(all_brand_links)
print(LENGTH_BRAND_LINKS)

paths = ["//h1[@class= 'pos_title']",
         "//div[@class = 'col-xl-12 default-description']/child::p[2]",
         "//div[@class = 'col-xl-12 default-description']/child::p[3]",
         "//div[@class = 'col-xl-12 default-description']/child::p[4]",
         "//div[@class = 'col-xl-12 default-description']/child::p[6]"]
try:
    with open('all_brands_data.csv', 'w', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['brand_name','brand_title','brand_description_one',
                         'brand_description_two','brand_description_three',
                         'important_notice','page_number'])
except IOError:
    pass


HOME_PAGE_LINKS = 'https://www.ozhat-turkiye.com/en/accustandard'
for item_name, page_link in all_brand_links.items():
    item_list = []
    home_page = requests.get(page_link, timeout=10)
    tree_home = html.fromstring(home_page.content)
    for path in paths:
        all_pages = tree_home.xpath(path)
        if len(all_pages) > 0:
            TEXT_DATA = all_pages[0].text_content()
        else:
            TEXT_DATA = "! No data available"
        item_list.append(TEXT_DATA)
    with open('all_brands_data.csv', 'a', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([item_name,item_list[0],item_list[1],
                         item_list[2],item_list[3],item_list[4],page_link])
