import requests #调用库
from bs4 import BeautifulSoup   #调用库
import csv   #调用库
#import codecs
with open ('new.csv','a',encoding='utf-8')as f: # 已增量的方式创建csv文件
    file = csv.writer(f)
    file.writerow(['name','data','content'])  #csv写入第一行表头数据
    f.close()
for i in range(500):   #生成1-499序列以改造网址
    id = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/comment-page-'+str(i)+'/'   #评论页一共有499页，每一页地址在网址中最后一个数字不一样，改造网页地址
    res = requests.get(str(id))   #向服务器请求网页
    html = res.text               #将网页代码转化为文本
    items = BeautifulSoup(html,'html.parser')      #转化为bs对象
    #item = items.find(class_='comments-title')
    #print(item.text)
    item1 = items.find_all(class_='comment byuser comment-author-spiderman even thread-even depth-1')  #在对象中查找符合查找条件的类
    for item2 in item1:    #遍历查到到的类
        name = item2.find(class_='fn')   #在类中继续查找符合条件的类
        data = item2.find(class_='comment-metadata')
        content = item2.find(class_='comment-content')
        #print(name.text,'\n',data.text,'\n',content.text)
        with open ('new.csv','a',encoding='gb18030',newline='') as b:  #避免乱码，编码写为gb18030
            #b.write(codecs.BOM_UTF8)
            file2 = csv.writer(b)
            file2.writerow([name.text,data.text,content.text])     #将类转化为文字并写入csv文件
            b.close()
