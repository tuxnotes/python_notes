import requests

r = requests.get('http://httpbin.org/headers')
r.context  # bytes形式
r.text  # 字符串
# 解析json数据

import json

d = json.loads(r.text) # 传入字符串而不是bytes

url = 'http://localhost:8050/render.html'
# 修改头部
headers = {'content-type': 'application/json'}
data = {'url': 'http://jd.com','timeout':20,'images':0}
# python对象不能直接上传，需要转换成json

json_data = json.dumps(data)
r2 = requests.post(url, headers=headers, data=json_data)
r2.text

# json.dump , json.load操作对象是文件

f = open('demo.json','w')
json.dump(data,f)
f.close()
f2 = open('demo.json')
json.load(f2) # 返回Python对象


