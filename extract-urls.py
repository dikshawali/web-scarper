from bs4 import BeautifulSoup
import requests
import pandas as pd

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
url='https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'

webpage=requests.get(url, headers=HEADERS)
soup=BeautifulSoup(webpage.content, "html.parser")
# print(soup)
print(str(soup)[0:])
links = soup.find_all("div",attrs={"data-component-type": 's-search-result'})
# print(soup)
# print(links)
i=0
for link in links:
    l = link.find_all("div",attrs={"class": 'sg-col-inner'})
    # print('data-asin:'+str(link.get('data-asin')))
    print(l)
    # print()
    i=i+1
# inner_links = links.find_all("div",attrs={"data-component-type": 's-search-result'})
