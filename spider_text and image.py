from http.client import REQUEST_URI_TOO_LONG
from wsgiref import headers
import requests

def spider_monga():
    url = 'https://www.bilibili.com/v/douga'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    request_info = requests.get(url, headers=header)
    print(request_info.text)

def spider_series():
    url = 'https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=1'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    request_info = requests.get(url, headers=header)
    for i in request_info.json().get('result').get('list'):
        print(i.get('title'))

def spider_img():
    url = 'https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=1'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    request_info = requests.get(url, headers=header)
    count = 0
    for i in request_info.json().get('result').get('list'):
        count += 1
        with open(f'./session 26/img{count}.png','wb') as file:
            img_info = requests.get(i.get('cover'), headers=header)
            file.write(img_info.content)


if __name__ == '__main__':
    spider_img()
    spider_monga()
    spider_series()