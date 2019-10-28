from urllib.request import quote
import requests
from bs4 import BeautifulSoup
while True:
    try:
        name = input('请输入您要下载的电影名称：')
        print('系统搜索中，请稍后')
        name1 = name.encode('gbk')
        url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(name1)
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
            thunder = soup1.find('div',id="Zoom").find('span').find('table').find('a')['href']
            print(name1+'的迅雷下载链接是：'+thunder,'\n','','\n',name1+'的磁力下载链接是：'+bt)
        else:
            print('网站没有收录'+ name +'这部影片')
    except:
        print('程序错误，请更换名称')
        pass

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
