from bs4 import BeautifulSoup
import requests
import pandas as pd

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

url='https://amazon.in/sspa/click?ie=UTF8&spc=MTo2MzI3NTI0MDk5ODMzOTMwOjE2NzU1NzEzNDg6c3BfbXRmOjIwMTEwNDgzMjI0MDk4OjowOjo&url=%2FNorthzone-Waterproof-Backpack-Business-Dimensions%2Fdp%2FB0BS6QQZYN%2Fref%3Dsr_1_11_sspa%3Fcrid%3D2M096C61O4MLT%26keywords%3Dbags%26qid%3D1675571348%26sprefix%3Dba%252Caps%252C283%26sr%3D8-11-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1'



webpage=requests.get(url, headers=HEADERS)
soup=BeautifulSoup(webpage.content, "html.parser")
# print(soup)
print(str(soup)[0:20])


try:
        title = soup.find("span",
                          attrs={"id": 'productTitle'})
        title_value = title.string
 
        title_string = title_value.strip().replace(',', '')
           
except AttributeError:
 
        title_string = "NA"
 
print("product Title = ", title_string)

#finding price

try:
    price=soup.find("span",attrs={"class": 'a-price-whole'})
    price_value=price.string
except:
    price_value='NA'
print('product price=', price_value)


#finding ratings

try:
    rating=soup.find_all("span", attrs={'class':'a-icon-alt'})[0]
    rating_value=rating.string
except:
    rating_value='NA'

print('product rating=', rating_value)


#Number of ratings

try:
    rating_number=soup.find_all("span", attrs={'id':'acrCustomerReviewText'})[0]
    rating_number_value=rating_number.string
except:
    rating_number_value='NA'

print("Number of ratings:", rating_number_value)