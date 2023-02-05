from bs4 import BeautifulSoup
import requests
import pandas as pd
import extractProdInfo as epi

def all_data():

    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    url='https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'

    webpage=requests.get(url, headers=HEADERS)
    soup=BeautifulSoup(webpage.content, "html.parser")
    # print(soup)
    # print(str(soup)[0:20])
    links = soup.find_all("div",attrs={"data-component-type": 's-search-result'})
    # print(soup)
    # link2=links[0].find_all('div', attrs={'class':'sg-col-inner'})[0].\
    #                 find_all('div', attrs={'data-csa-op-log-render':''})[0].\
    #                 find_all('div', attrs={'class':'rush-component'})[0].\
    #                 find_all('div',attrs={'data-component-type':'s-impression-counter'})[0].\
    #                 find_all('div', attrs={'class':'s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border'})[0].\
    #                 find_all('div', attrs={'class':'a-section'})[0].\
    #                 find_all('div', attrs={'class':'sg-row'})[0].\
    #                 find_all('div', attrs={'class':'sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-4-of-20 s-list-col-left'})[0].\
    #                 find_all('div', attrs={'class':'sg-col-inner'})[0].\
    #                 find_all('div', attrs={'class':'s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small s-flex-expand-height'})[0].\
    #                 find_all('div', attrs={'class':'aok-relative'})[0].\
    #                 find_all('span', attrs={'data-component-type': 's-product-image'})[0].\
    #                 find_all('a', attrs={'class': 'a-link-normal s-no-outline'})[0].get('href')
    # print(link2)
    # i=0
    # l = links.find_all("div",attrs={"class": 'sg-col-inner'})
    # for link in links:
        # l = link.find_all("div",attrs={"class": 'sg-col-inner'}).find_all("div", attrs={'data-csa-op-log-render': ''}).get('data-cel-widget')
        # print('data-asin:'+str(link.get('data-asin')))
        # print('data-asin:'+str(l))
        # print()
        # i=i+1
    # inner_links = links.find_all("div",attrs={"data-component-type": 's-search-result'})
    main_res=[['product ASIN', 'URL', 'Title', 'Price', 'Ratings', 'Number of ratings']]

    for link in links:
        try:
            # print('data-asin:'+str(link.get('data-asin')))
            result=[]
            result.append(str(link.get('data-asin')))
            link2=link.find_all('div', attrs={'class':'sg-col-inner'})[0].\
                    find_all('div', attrs={'data-csa-op-log-render':''})[0].\
                    find_all('div', attrs={'class':'rush-component'})[0].\
                    find_all('div',attrs={'data-component-type':'s-impression-counter'})[0].\
                    find_all('div', attrs={'class':'s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border'})[0].\
                    find_all('div', attrs={'class':'a-section'})[0].\
                    find_all('div', attrs={'class':'sg-row'})[0].\
                    find_all('div', attrs={'class':'sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-4-of-20 s-list-col-left'})[0].\
                    find_all('div', attrs={'class':'sg-col-inner'})[0].\
                    find_all('div', attrs={'class':'s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small s-flex-expand-height'})[0].\
                    find_all('div', attrs={'class':'aok-relative'})[0].\
                    find_all('span', attrs={'data-component-type': 's-product-image'})[0].\
                    find_all('a', attrs={'class': 'a-link-normal s-no-outline'})[0]
            # print('product-link'+str(link2.get('href')))
            result.append(str(link2.get('href')))
            if not str(link2.get('href'))=='':
                title_string, price_value, rating_value, rating_number_value=epi.prod_url('https://www.amazon.in'+str(link2.get('href')))
                result.append(title_string)
                result.append(price_value)
                result.append(rating_value)
                result.append(rating_number_value)
            # for r in result:
            #         print(r)
            main_res.append(result)
        except:
            pass
    return main_res
