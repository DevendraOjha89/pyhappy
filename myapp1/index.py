import requests
from bs4 import BeautifulSoup
request_flipkart = requests.get("https://www.flipkart.com/asus-vivobook-14-ryzen-5-quad-core-2nd-gen-8-gb-512-gb-ssd-windows-10-home-x412da-ek503t-thin-light-laptop/p/itm5b6707a02a046?pid=COMFMCSBFCDGSPZK&lid=LSTCOMFMCSBFCDGSPZKR8TCAF&otracker=hp_banner_3_5.bannerX3.BANNER_2LBP3ZBVG2PE&fm=neo%2Fmerchandising&iid=M_3220729f-7765-4703-970d-6e74ce0282d1_5.2LBP3ZBVG2PE&ssid=keb1ahoag00000001580288849111")

#print(request_flipkart.text)
tree_flipkart = BeautifulSoup(request_flipkart.text,features="lxml")
result_flipkart = tree_flipkart.find("div", {"class":"_1vC4OE _3qQ9m1"})

#request_amazon = requests.get("https://www.amazon.in/VivoBook-M409DA-EK146T-Integrated-Graphics-Transparent/dp/B082PB9GDN/ref=sr_1_1_sspa?keywords=Asus+VivoBook&qid=1580289323&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNVRFOFdYMldVTzVSJmVuY3J5cHRlZElkPUEwMTg1OTI0MUlTQ0U1QkJQRDFMNiZlbmNyeXB0ZWRBZElkPUEwNTMxMjQ3M1NBOE5DTDdPVUw0TSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
request_amazon = requests.get("https://www.amazon.in/VivoBook-M409DA-EK146T-Integrated-Graphics-Transparent/dp/B082PB9GDN/ref=sr_1_1_sspa?keywords=Asus+VivoBook&qid=1580289323&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNVRFOFdYMldVTzVSJmVuY3J5cHRlZElkPUEwMTg1OTI0MUlTQ0U1QkJQRDFMNiZlbmNyeXB0ZWRBZElkPUEwNTMxMjQ3M1NBOE5DTDdPVUw0TSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"})
tree_amazon = BeautifulSoup(request_amazon.text,features="lxml")
result_amazon = tree_amazon.find("span", {"class":"a-size-medium a-color-price priceBlockBuyingPriceString"})

print(tree_flipkart.title)
print(result_flipkart.text)

print(tree_amazon.title)
print(result_amazon.text[2:8].replace(",",""))

print("Difference amount is : ")

print(int(result_flipkart.text[1:].replace(",", ""))-int(result_amazon.text[2:8].replace(",","")))