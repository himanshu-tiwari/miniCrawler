import requests
from bs4 import BeautifulSoup

def spidey(count):
    i = 1
    while i <= count:
        url = 'http://www.buckyslockerroom.com/Wisconsin_Badgers/pg/' + str(i) + '/ps/60/so/no_sort'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        urls = 1
        for link in soup.findAll('a', {'class': 'browseProductLink'}):
            while urls <= 5:
                urls+=1
                href = link.get('href')
                #print(href)
                get_single_item_data(href)
            urls=1
        i+=1

def get_single_item_data(item_url):
    url = 'http://www.buckyslockerroom.com' + item_url
    #print(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('title'):
        print(item_name.string)

spidey(1)