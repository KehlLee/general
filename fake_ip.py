import imp
import os
path = os.getcwd()
baidu_search = imp.load_source('search', path+'/baidu_search_folder/baidu_search.py')
# import requests
# baidu_search.baidu_search('青蛙')
baidu_search.baidu_search()

print(path)
