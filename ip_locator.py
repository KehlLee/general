
import requests
from lxml import etree



def locate_ip():
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    header = {
        'User-Agent':ua
    }
    param = {
        'wd':'IP地址查询'
    }
    fake_ip = '114.215.174.98:16819'
    proxy = {
        'http':f'http://{fake_ip}',
        'https':f'http://{fake_ip}'
    }
    s = requests.session()
    s.keep_alive = False
    request_info = requests.get(url=url, headers=header, proxies=proxy, params=param)
    # request_info.encoding = request_info.apparent_encoding
    # print(request_info.text)
    # print(request_info.status_code)
    # with open('fake_ip.html', 'w') as fp:
    #     fp.write(request_info)
    with open('fake_ip.html', 'w', encoding='utf-8') as file:
        file.write(request_info.text)


if __name__ == '__main__':
    locate_ip()