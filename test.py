# //div[@class = 'col-xl-12 default-description']/child::p[2]

# "//h1[@class= 'pos_title']",
"""This program extracts data from Ozhat.com including all brand products."""
import csv
from lxml import html
import requests


# home_page_links = 'https://www.ozhat-turkiye.com/en/accustandard'
# home_page = requests.get(home_page_links,timeout=10)
# tree_home = html.fromstring(home_page.content)
# all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[2]")
# text = all_pages[0].text_content()
#
# print(text)


# //div[@class = 'col-xl-12 default-description']/child::p[2]
# "//img[@alt= 'AccuStandard']

"""This program extracts data from Ozhat.com including all brand products."""
import csv
from lxml import html
import requests

paths = ["//div[@class = 'col-xl-12 default-description']/child::p[2]",
         "//div[@class = 'col-xl-12 default-description']/child::p[3]",
         "//div[@class = 'col-xl-12 default-description']/child::p[4]",
         "//div[@class = 'col-xl-12 default-description']/child::p[6]"]

# //h1[@class = 'pos_title']

product_data = []
home_page_links = 'https://www.ozhat-turkiye.com/en/4b-braime'
home_page = requests.get(home_page_links, timeout=10)
tree_home = html.fromstring(home_page.content)
all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[2]")
text = all_pages[0].text_content()
all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[3]")
text1 = all_pages[0].text_content()
all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[4]")
text2 = all_pages[0].text_content()
all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[6]")
text3 = all_pages[0].text_content()

# for item in product_data:
#     print(item)
#     print()
#     print()
print(text.strip())
print()
print()
print()
print(text1.strip())
print()
print()
print()
print(text2.strip())
print()
print()
print()
print(text3.strip())

    # all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[3]")
    # text1 = all_pages[0].text_content()
    # all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[4]")
    # text2 = all_pages[0].text_content()
    # all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[6]")
    # text3 = all_pages[0].text_content()
# /html/body/div[3]/div/div[1]/div[1]/div/div[2]/div/div/p[7]



# home_page_links = 'https://www.ozhat-turkiye.com/en/accustandard'
# home_page = requests.get(home_page_links, timeout=10)
# tree_home = html.fromstring(home_page.content)
# all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[2]")
# text = all_pages[0].text_content()
# all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[3]")
# text1 = all_pages[0].text_content()
# all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[4]")
# text2 = all_pages[0].text_content()
# all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[6]")
# text3 = all_pages[0].text_content()


"""from this is brand data scraper"""

# counter = 1
# home_page_links = 'https://www.ozhat-turkiye.com/en/accustandard'
# for item_name, page_link in all_brand_links.items():
#     home_page = requests.get(page_link, timeout=10)
#     tree_home = html.fromstring(home_page.content)
#
#     all_pages = tree_home.xpath("//h1[@class= 'pos_title']")
#     if len(all_pages) > 0:
#         title_brand = all_pages[0].text_content()
#     else:
#         title_brand = "! No data available"
#
#     all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[2]")
#     if len(all_pages) > 0:
#         text = all_pages[0].text_content()
#     else:
#         text = "! No data available"
#
#     all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[3]")
#     if len(all_pages) > 0:
#         text1 = all_pages[0].text_content()
#     else:
#         text1 = "! No data available"
#
#     all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[4]")
#     if len(all_pages) > 0:
#         text2 = all_pages[0].text_content()
#     else:
#         text2 = "! No data available"
#
#     all_pages = tree_home.xpath("//div[@class = 'col-xl-12 default-description']/child::p[6]")
#     if len(all_pages) > 0:
#         text3 = all_pages[0].text_content()
#     else:
#         text3 = "! No data available"
#
#
#     print("Item number " + str(counter))
#     print(title_brand.strip())
#     print()
#     print(text.strip())
#     print()
#     print(text1.strip())
#     print()
#     print(text2.strip())
#     print()
#     print(text3.strip())
#     print()
#     counter = counter + 1
#     if counter == 20 :
#         exit()