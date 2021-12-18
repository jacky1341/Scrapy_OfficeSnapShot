import requests
import re
from lxml import etree
import csv
import time
import random

headers = {
    'Referer':'https://officesnapshots.com/',
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
base_url = 'https://officesnapshots.com/offices/?browse_page={}&filter_location=united-states'


r_list = []
for i in range(1, 11):
    url = base_url.format(i)
    html = requests.get(url, headers=headers).text
    time.sleep(random.uniform(1, 3))
    obj = etree.HTML(html)
    r_list.append(obj.xpath('//*[@id="offices"]'))
print(r_list)

result = []
for i in r_list:
    result.append(i[0].xpath('./div/a/@href'))


with open('office_snap.csv', 'w') as f:
    writer = csv.writer(f)
    for i in result:
        for j in i:
            two_html = requests.get(url=j, headers=headers).text
            obj = etree.HTML(two_html)
            sec_link = obj.xpath('//*[@id="content"]/div/div/p/a/@href')
            print(sec_link[0])
            writer.writerow([sec_link[0]])
        time.sleep(random.uniform(1, 3))







