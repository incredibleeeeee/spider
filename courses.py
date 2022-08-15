import requests
import json

url = 'https://jwxt.nwpu.edu.cn/course-selection-api/api/v1/student/course-select/selected-lessons'
url1 = 'https://jwxt.nwpu.edu.cn/course-selection-api/api/v1/student/course-select/std-count'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'jwxt.nwpu.edu.cn',
    'Referer': 'https://jwxt.nwpu.edu.cn/course-selection/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.3',

}

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'

response = json.loads(response.text)['data']

id = []
cource_name = []
limitCount = []

for i in response:
    id.append(i['id'])
    cource_name.append(i['course']['nameZh'])
    limitCount.append(i['limitCount'])

print(id)
print(cource_name)
print(limitCount)

para = {
    'lessonIds': '0',
}

for i in range(0, len(id)):
    para['lessonIds'] = id[i]
    response = requests.get(url=url1, headers=headers, params=para)
    response.encoding = 'utf-8'
    response = json.loads(response.text)
    sum = response['data']['{}'.format(id[i])]
    print(str(sum) + '/' + str(limitCount[i]))
