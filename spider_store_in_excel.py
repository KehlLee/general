from openpyxl import Workbook
from pyparsing import WordEnd
import requests
import re
from lxml import etree

def spider_store_in_file_using_re():
    url = 'https://www.bilibili.com/v/popular/rank/bangumi?spm_id_from=333.1007.0.0'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    request_info = requests.get(url, headers = header)
    names = re.findall('<a href=".+" target="_blank" class="title">(.+)</a>', request_info.text)
    # for name in names:
    #     print(name)
    views = re.findall('''<img src=".+" alt="play">
    (.+)
    ''', request_info.text)
    likes = re.findall('''<img src=".+" alt="follow">
    (.+)
    ''', request_info.text)
    updates = re.findall('''<div class="detail"><span class="data-box">
    (.+)
    ''', request_info.text)
    # for view in views:
        # print(view.strip())
    info_list = []
    # print(len(names), len(views), len(likes), len(updates))
    for i in range(len(names)):
        info_list.append([names[i], views[i].strip(), likes[i].strip(), updates[i].strip()])
    # for row in info_list:
    #     print(row)

    wb = Workbook()
    sh = wb.active
    for row in info_list:
        sh.append(row)
    wb.save('./session 29/统计结果.xlsx')

def spider_store_in_file_using_lxml():
    url = 'https://www.bilibili.com/v/popular/rank/bangumi?spm_id_from=333.1007.0.0'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    request_info = requests.get(url, headers = header)
    e = etree.HTML(request_info.text)
    names = e.xpath('//div[@class="info"]/a/text()')
    views = e.xpath('//div[@class="detail-state"]/span[1]/text()')
    likes = e.xpath('//div[@class="detail-state"]/span[2]/text()')
    updates = e.xpath('//div[@class="detail"]/span[@class="data-box"]/text()')
    info_list = []
    # print(len(names), len(views), len(likes), len(updates))
    for i in range(len(names)):
        info_list.append([names[i], views[i].strip(), likes[i].strip(), updates[i].strip()])
    # for row in info_list:
    #     print(row)

    wb = Workbook()
    sh = wb.active
    for row in info_list:
        sh.append(row)
    wb.save('./session 29/统计结果(lxml).xlsx')

if __name__ == '__main__':
    # spider_store_in_file_using_re()
    spider_store_in_file_using_lxml()
