# -*- coding: utf-8 -*-
# author:laidefa

# 载入包
import requests
import json
import time

params={
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}


url='http://127.0.0.1:8000/sys/sinoma/v1/optimization/predict/fcao'

time1=time.time()
html = requests.post(url, json.dumps(params))
print(json.dumps(params))
print('发送post数据请求成功!\n{}'.format(html.url))
print('返回post结果如下：')
print(html.text)

time2=time.time()
print('总共耗时：' + str(time2 - time1) + 's')
