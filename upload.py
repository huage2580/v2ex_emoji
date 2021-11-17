
# 上传图片
import requests
import os
import json

resultMap = {}

def upload_file(filename):
    url = "http://127.0.0.1:36677/upload"
    path = os.getcwd()+'\\emoji\\'+filename
    # path = path.replace('\\', "/")
    data = json.dumps({"list": [path]})
    # print(data)
    r = requests.post(url, data=data)
    output_img = r.json()['result'][0]
    return output_img


# 检查有没有上传过
if os.path.exists("map.txt"):
    with open("map.txt","r",encoding='utf-8') as f:
        txt = f.read()
        resultMap = json.loads(txt)
# print(resultMap)

for icon in os.listdir('emoji'):
    k = icon.replace('.png','')
    if resultMap.__contains__(k):
        print('已上传')
        continue
    result = upload_file(icon)
    resultMap[k] = result
    print('upload success:'+icon)
    with open("map.txt","w",encoding='utf-8') as f:
        f.write(json.dumps(resultMap))


print('完成！')