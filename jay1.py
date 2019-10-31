import requests
res = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010')
pinglun = res.json()
pinglun1 = pinglun['hot_comment']['commentlist']
for i in pinglun1:
    pinglun2 = i['rootcommentcontent']
    print(pinglun2)
    print('-------------------------------------------------')
for x in range(1,4):
    res1 = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=8&needmusiccrit=0&pagenum='+str(x)+'&pagesize=15&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010')
    pinglun2 = res1.json()
    pinglun3 = pinglun2['comment']['commentlist']
    y = 0
    for b in pinglun3:
        pinglun4 = b['rootcommentcontent']
        print(str(y)+'、'+pinglun4)
        print('-------------------------------------------------')
        


