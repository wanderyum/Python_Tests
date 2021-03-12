import requests
import json

url_base = 'http://127.0.0.1:8000'

param0 = {'l': 'loc', 's': 'data'}
url0 = url_base + '/get_data'
print('测试1:\n{}'.format(url0))
resp0 = requests.get(url0, params=param0)
print('content: {}'.format(resp0.content))
print('text: {}'.format(resp0.text))

param1 = {'name': 'name1', 'price': 6.6}
url1 = url_base + '/post_data'
print('测试2:\n{}'.format(url1))
resp1 = requests.post(url1, data=json.dumps(param1))
print(resp1.url)
print('content: {}'.format(resp1.content))
print('text: {}'.format(resp1.text))