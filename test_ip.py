import requests

url = 'http://whois.pconline.com.cn/ipJson.jsp?json=true'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
}

response = requests.post(url=url, headers=headers)
response.encoding = 'gbk'
response_text = response.text

print(response_text)
