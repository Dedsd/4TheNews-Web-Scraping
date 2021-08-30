from os import name
from typing import ValuesView
from urllib.parse import urljoin
from urllib.request import URLopener, urlopen
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import random

fkheader = UserAgent()
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def newsen():
    website = BeautifulSoup(session.get(f'https://www.bbc.com/news/world',
                                        headers={"User-Agent": str(fkheader.random)}).content, "html.parser")
    lista_links = []
    for a in website.find_all('a', href=True):
        try:
            if a['href'][-1].isdigit():
                if a['href'].startswith('/news/world'):
                    lista_links.append(f"https://www.bbc.com{a['href']}")
        except IndexError:
            break

    news1 = random.choice(lista_links)
    lista_links.remove(news1)
    news2 = random.choice(lista_links)

    html1 = requests.get(news1).text
    soup = BeautifulSoup(html1, 'html.parser')

    title1 = soup.find_all('title')
    title2 = soup.findAll('meta')


    title111 = title1[0].text
    stitle = str(title2[2])[str(title2[2]).find('"'):str(title2[2]).find('.')].replace('"', '')
    print("-----------------------------------------------------------------------------------")
    html3 = requests.get(news2).text
    soup3 = BeautifulSoup(html3, 'html.parser')

    title5 = soup3.find_all('title')
    title6 = soup3.findAll('meta')


    title122 = title5[0].text
    stitle1 = str(title6[2])[str(title6[2]).find('"'):str(title6[2]).find('.')].replace('"', '')

    website2 = BeautifulSoup(session.get(f'https://www.bbc.com/news/technology',
                                        headers={"User-Agent": str(fkheader.random)}).content, "html.parser")
    lista_links2 = []
    for a in website2.find_all('a', href=True):
        try:
            if a['href'][-1].isdigit():
                if a['href'].startswith('/news/technology'):
                    lista_links2.append(f"https://www.bbc.com{a['href']}")
        except IndexError:
            break

    news3 = random.choice(lista_links2)
    lista_links2.remove(news3)
    news4 = random.choice(lista_links2)

    html2 = requests.get(news3).text
    soup2 = BeautifulSoup(html2, 'html.parser')

    title3 = soup2.find_all('title')
    title4 = soup2.findAll('meta')

    title133 = title3[0].text
    stitle2 = str(title4[2])[str(title4[2]).find('"'):str(title4[2]).find('.')].replace('"', '')
    print("-----------------------------------------------------------------------------------")
    html4 = requests.get(news4).text
    soup4 = BeautifulSoup(html4, 'html.parser')

    title7 = soup4.find_all('title')
    title8 = soup4.findAll('meta')

    title144 = title7[0].text
    stitle3 = str(title8[2])[str(title8[2]).find('"'):str(title8[2]).find('.')].replace('"', '')
    return {
        "newsen()": newsen(),
        "title111": title111,
        "stitle": stitle,
        "news1": news1,
        "title122": title122,
        "stitle1": stitle1,
        "news2": news2,
        "title133": title133,
        "stitle2": stitle2,
        "news3": news3,
        "title144": title144,
        "stitle3": stitle3,
        "news4": news4
    }

def newsbr():
    website3 = BeautifulSoup(session.get(f'https://www.bbc.com/portuguese',
                                        headers={"User-Agent": str(fkheader.random)}).content, "html.parser")
    lista_links3 = []
    for a in website3.find_all('a', href=True):
        try:
            if a['href'][-1].isdigit():
                if a['href'].startswith('/portuguese'):
                    lista_links3.append(f"https://www.bbc.com{a['href']}")
        except IndexError:
            break

    news5 = random.choice(lista_links3)
    lista_links3.remove(news5)
    news6 = random.choice(lista_links3)

    html5 = requests.get(news5).text
    soup6 = BeautifulSoup(html5, 'html.parser')

    title9 = soup6.find_all('title')
    title10 = soup6.findAll('meta')

    title111br = title9[0].text
    stitlebr = str(title10[7])[str(title10[7]).find('"'):str(title10[7]).find('.')].replace('"', '')
    print("-----------------------------------------------------------------------------------")
    html6 = requests.get(news6).text
    soup7 = BeautifulSoup(html6, 'html.parser')

    title11 = soup7.find_all('title')
    title12 = soup7.findAll('meta')

    title122br = title11[0].text
    stitle1br = str(title12[7])[str(title12[7]).find('"'):str(title12[7]).find('.')].replace('"', '')

    website4 = BeautifulSoup(session.get(f'https://www.bbc.com/portuguese/topics/c404v027pd4t',
                                        headers={"User-Agent": str(fkheader.random)}).content, "html.parser")
    lista_links4 = []
    for a in website4.find_all('a', href=True):
        try:
            if a['href'][-1].isdigit():
                if a['href'].startswith('/portuguese'):
                    lista_links4.append(f"https://www.bbc.com{a['href']}")
        except IndexError:
            break

    news8 = random.choice(lista_links4)
    lista_links4.remove(news8)
    news9 = random.choice(lista_links4)

    html7 = requests.get(news8).text
    soup8 = BeautifulSoup(html7, 'html.parser')

    title13 = soup8.find_all('title')
    title14 = soup8.findAll('meta')

    title133br = title13[0].text
    stitle2br = str(title14[7])[str(title14[7]).find('"'):str(title14[7]).find('.')].replace('"', '')
    print("-----------------------------------------------------------------------------------")
    html8 = requests.get(news9).text
    soup9 = BeautifulSoup(html8, 'html.parser')

    title15 = soup9.find_all('title')
    title16 = soup9.findAll('meta')

    title144br = title15[0].text
    stitle3br = str(title16[7])[str(title16[7]).find('"'):str(title16[7]).find('.')].replace('"', '')
    return {
        "newsbr()": newsbr(),
        "title111br": title111br,
        "stitlebr": stitlebr,
        "news5": news5,
        "title122br": title122br,
        "stitle1br": stitle1br,
        "news6": news6,
        "title133br": title133br,
        "stitle2br": stitle3br,
        "news8": news8,
        "title144br": title144br,
        "stitle3br": stitle3br,
        "news9": news9,
    }