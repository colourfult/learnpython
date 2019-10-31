from urllib.request import quote
import requests
from bs4 import BeautifulSoup
while True:
    #try:
    print('------------欢迎使用电影搜索器------------')
    choice1 = int(input('请输入您要搜索的类型：1、电影    2、电视剧    3、综艺    4、动漫'))
    if choice1 == 1:
        choice2 =1
    elif choice1 ==2:
        choice2 =2
    elif choice1 ==3:
        choice2 = 99
    elif choice1 == 4:
        choice2 = 16
    name = input('请输入您要下载的电影名称：')
    print('系统搜索中，请稍后')
    name1 = name.encode('gbk')
    url = 'http://s.ygdy8.com/plus/so.php?typeid='+str(choice2)+'&keyword='+quote(name1)
    res = requests.get(url)
    res.encoding = 'gbk'
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    item = soup.find('div',class_='co_content8').find_all('table')
    print('')
    print('-------------'+name+'的搜索结果是-------------')
    if item:
        i = 0
        print('搜索到的影片有：')
        for items in item:
            name = items.find('a').text
            i = i+1
            print(str(i)+'、'+name)
        choice = int(input('请输入您要下载的影片序号：'))
        name1 = item[int(choice-1)].find('a').text
        url1 = 'https://www.ygdy8.com'+item[int(choice-1)].find('a')['href']
        movie = requests.get(url1)
        movie.encoding = 'gbk'
        html1 = movie.text
        soup1 = BeautifulSoup(html1,'html.parser')
        bt = soup1.find('div',id="Zoom").find('span').find('a')['href']
        thunders = soup1.find('div',id="Zoom").find('span').find_all('table')
        if choice1 == 1:
            print(name1+'的磁力下载链接是：'+bt,'\n',name1+'的迅雷下载链接是：')
            x = 0
            for thunder in thunders:
                thunder_url =thunder.find('a')['href']
                x = x+1
                print('第'+str(x)+'集、'+thunder_url)
        else:
            x = 0
            print(name1+'的迅雷下载链接是：')
            for thunder in thunders:
                thunder_url =thunder.find('a')['href']
                x = x+1
                print('第'+str(x)+'集、'+thunder_url)
            
    else:
        print('网站没有收录'+ name +'这部影片')
    #except:
        #print('程序错误，请更换名称')
       # pass

    goon = input('再来一发？Y继续，任意键退出')

    if goon == 'y':
        continue
    else:
        print('感谢使用本程序')
        break

'''
更新说明：
1、解决了搜索同一个关键字出现多部影片的情况。
'''
