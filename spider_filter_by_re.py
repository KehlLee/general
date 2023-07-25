import re
import requests

def spider_animation():
    url = 'https://www.bilibili.com/v/popular/rank/douga?spm_id_from=333.1007.0.0'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    request_info = requests.get(url, headers = header)
    titles = re.findall('<a href=".+" target="_blank" class="title">(.+)</a>', request_info.text)
    views = re.findall('''<span class="data-box"><img src=".+" alt="play">
        (.+)
        ''', request_info.text)
    comments = re.findall('''<span class="data-box"><img src=".+" alt="like">
        (.+)
        ''', request_info.text)
    for title, view, comment in zip(titles, views, comments):
        print(f'=={title}=={view.strip()}=={comment.strip()}==')
    # print(request_info.text)

spider_animation()