from dataclasses import replace
import requests
from bs4 import BeautifulSoup

def get_rate():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp' 
    r = requests.get(url)
    #lxml gives more performance than html
    soup = BeautifulSoup(r.content, 'lxml-xml') 
    #We search by currency id, then find the rate value
    rate_str = soup.find(ID ='R01235').find('Value').text
    #Casting a value to a type float and return
    return float(rate_str.replace(',', '.'))


if '__main__' == __name__:
    print(f'usd: {get_rate()}')