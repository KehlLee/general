from lxml import etree
import requests

def spider_left_bar_content():
    url = 'https://itbaizhan.com'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    request_info = requests.get(url, headers = header)
    e = etree.HTML(request_info.text)
    categoties = e.xpath('//ul[@class="clearfix"]/li/a/text()')
    for category in categoties:
        print(category)

def spider_animation():
    url = 'https://www.bilibili.com/v/popular/rank/douga?spm_id_from=333.1007.0.0'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    request_info = requests.get(url, headers = header)
    e = etree.HTML(request_info.text)
    titles = e.xpath('//a[@class="title"]/text()')
    views = e.xpath('//div[@class="detail-state"]/span[1]/text()')
    comments = e.xpath('//div[@class="detail-state"]/span[2]/text()')
    for title, view, comment in zip(titles, views, comments):
        print(f'{title}=={view.strip()}=={comment.strip()}')


if __name__ == '__main__':
    spider_animation()
    spider_left_bar_content()