import requests
num = input('请输入单号：')
url = 'https://www.kuaidi100.com/query'
params = {
    'type': 'jd',
'postid': str(num),
'temp': '0.9186509975044364',
'phone': '',
}
headers = {
    'Host': 'www.kuaidi100.com',
'Referer': 'https://www.kuaidi100.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
}
res = requests.get(url,params=params,headers=headers)
msg = res.json()['message']
check = res.json()['data']
if msg == 'ok':
    for info in check:
        a = info['context']
        time = info['time']
        print('时间：'+time+'*'+a)
else:
    print(msg)
