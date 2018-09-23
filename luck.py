#! python3

import requests
from bs4 import BeautifulSoup
import os

all_url = 'http://www.mzitu.com'


#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'
               }
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'
}
#此请求头破解盗链

start_html = requests.get(all_url,headers = Hostreferer)

#保存地址
path = '/home/lyt/mzitu/'
some = 25625
w = "wijf"
#找寻最大页数
soup = BeautifulSoup(start_html.text,"html.parser")
page = soup.find_all('a',class_='page-numbers')
print(str(page[3]))
max_page = page[-2].text
print(max_page)

