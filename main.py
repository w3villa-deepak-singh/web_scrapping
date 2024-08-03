import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/s?k=oppo&crid=1NUIVTMSQXCOT&sprefix=oppo%2Caps%2C278&ref=nb_sb_noss_1"
proxies = {
    "http" : "http://109.125.132.244"
}
response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.text , "html.parser")
# print(soup.find_all(class_="KzDlHZ"))
for data in soup.find_all(class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2") :
    print(data.text)
for data in soup.find_all(class_="a-price-whole") :
    print(data.text)
