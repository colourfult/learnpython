import os,base64,requests,json,time
session = requests.session()
url = 'https://h5.ele.me/restapi/eus/v3/captchas'
phone_num = input('请输入手机号')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}
data = {
    'captcha_str': phone_num
}
res=requests.post(url,headers=headers,data=data)#这里模拟输入手机号
yanzhengma = res.json()
cap_hash = yanzhengma['captcha_hash']
cap_img = yanzhengma['captcha_image']
str_img = cap_img[23:]#这里获取验证码base64图片代码
img = base64.b64decode(str_img)#将base64代码解码转换为图片
fh = open('pic.jpg','wb')#将图片保存，以便打开查看图片验证码，暂不知怎样自动识别
fh.write(img)
fh.close()
pic_yanzheng = input('请输入图片验证码')
url1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
data1 ={
    'captcha_hash': cap_hash,
'captcha_value': pic_yanzheng,
'mobile': phone_num,
'scf': 'ms',
}
res1 = session.post(url1,headers=headers,data=data1)#使用图片验证码和手机号请求手机验证码
yanzhengma1 = res1.json()
va_token = yanzhengma1['validate_token']
url2 ='https://h5.ele.me/restapi/eus/login/login_by_mobile'
data2 = {
    'mobile': phone_num,
'scf': 'ms',
'validate_code': input('请输入手机验证码'),
'validate_token':va_token,
}
session.post(url2,headers=headers,data=data2)#将cookie存入session并模拟登陆
url3 ='https://www.ele.me/restapi/shopping/v1/cities/guess'
guess1 = requests.get(url3,headers=headers)
guess = guess1.json()
latitude = guess['latitude']
longitude = guess['longitude']
url4 = 'https://www.ele.me/restapi/bgs/poi/search_poi_nearby'
params ={
    'geohash': 'ww0v9te1kuc7',
'keyword': input('请输入要搜索的地址：'),
'latitude': latitude,
'limit': '20',
'longitude': longitude,
'type': 'nearby',
}
res2 = requests.get(url4,headers=headers,params=params)#模拟输入搜索地址
address_all = res2.json()
for address in range(len(address_all)):
    print(str(address+1)+'、'+address_all[address]['address'])#打印出输入地址后系统提示的详细地址
address1 = int(input('请选择详细的地址：'))
address_select = address_all[address1-1]['geohash']
url5 = 'https://www.ele.me/restapi/shopping/restaurants'
params1 = {
    'extras[]': 'activities',
'geohash': 'ww0v9j735v05',
'latitude': guess['latitude'],
'limit': '24',
'longitude': guess['longitude'],
'offset': '0',
'restaurant_category_ids[]': '-100',
'restaurant_category_ids[]': '207',
'restaurant_category_ids[]': '220',
'restaurant_category_ids[]': '260',
'restaurant_category_ids[]': '233',
'restaurant_category_ids[]': '-102',
'restaurant_category_ids[]': '-103',
'restaurant_category_ids[]':'-104',
'restaurant_category_ids[]': '-105',
'restaurant_category_ids[]': '-107',
'restaurant_category_ids[]': '-106',
'terminal': 'web',
}
shops = session.get(url5,headers=headers,params=params1)#请求地址对应的商家名称
shops_json = shops.json()
for i in range(len(shops_json)):
    print(shops_json[i]['name'])
