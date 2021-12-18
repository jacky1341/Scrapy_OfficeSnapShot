import requests
import re
from lxml import etree
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
base_url = 'https://officesnapshots.com/offices/?browse_page={}&filter_location=united-states'

def crawl():
    r_list = []
    for i in range(1, 3):
        url = base_url.format(i)
        html = requests.get(url, headers=headers).text
        obj = etree.HTML(html)
        r_list.append(obj.xpath('//*[@id="offices"]'))
    print(r_list)
    return r_list




# def pahse(r_list):
#     result = []
#     url = []
#     for i in r_list:
#         result.append(i[0].xpath('./div/a/p[1]/text()'))
#         url.append(i[0].xpath('./div/a/@href'))
#     # print(result)
#     # print(url)
#     return result, url

# def save(result, url):
#     with open('office_snap.scv', 'w') as f:
#         writer = csv.writer(f)
#         print(len(result))
#         final = {}
#         for i in range(len(result)):
#             for page in range(len(result[i])):
#                 final[result[i][page]] = url[i][page]
#         return final

r_list = crawl()
# result, url = pahse(r_list)
# final = save(result, url)
# with open('office_snap.csv', 'w') as f:
#     writer = csv.writer(f)
#     for key, value in final.items():
#         print(key, value)
#         writer.writerow([key, value])
