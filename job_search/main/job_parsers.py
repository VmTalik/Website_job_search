import requests
from bs4 import BeautifulSoup
from random import randint

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
]


def superjob(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://www.superjob.ru'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            div_lst = soup.find_all('div', class_='_2lp1U _3NBrD _1WtQU')
            for div in div_lst:
                title = div.find('span', class_='_3FqEL _2JQOY _1dTXK _3h_V4 _1hdbq').find('a')
                jobs.append(title)
                # дописать
        else:
            errors.append({'url': url, 'title': "Div does not exists"})
    else:
        errors.append({'url': url, 'title': "Page do not response"})
    return jobs
