import requests
import html
listname = []
listid = []
listurl = []
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for i in range(1,6):
    params = {
'ct': '24',
'qqmusic_ver':'1298',
'new_json': '1',
'remoteplace': 'txt.yqq.song',
'searchid': '66330225152414321',
't': '0',
'aggr': '1',
'cr': '1',
'catZhida': '1',
'lossless': '0',
'flag_qc': '0',
'p': str(i),
'n': '10',
'w': '周杰伦',
'g_tk': '5381',
'loginUin': '0',
'hostUin': '0',
'format': 'json',
'inCharset': 'utf8',
'outCharset': 'utf-8',
'notice': '0',
'platform': 'yqq.json',
'needNewCode': '0'
}
    headers = {
'Origin': 'https://y.qq.com',
'Referer': 'https://y.qq.com/portal/search.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',        
    }
    res = requests.get(url,params=params,headers=headers)
    music_list = res.json()
    music_list1 = music_list['data']['song']['list']
    for song in music_list1:
        song_id = song['id']
        song_name = song['name']
        song_mid = ['mid']
        song_url = 'https://y.qq.com/n/yqq/song/'+str(song_mid)+'.html' 
        listid.append(song_id)
        listname.append(song_name)
        listurl.append(song_url)

for x in range(len(listid)):
    url1 = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
    params1 = {
        'nobase64': '1',
        'musicid': str(listid[x]),
        '-': 'jsonp1',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        }
    headers1 = {
        'Origin': 'https://y.qq.com',
        'Referer': listurl[x],        
        }
    res1 = requests.get(url1,params=params1,headers=headers1)
    song_lyric = res1.json()['lyric']
    format_lyric = html.unescape(song_lyric)
    print('歌曲名：'+listname[x],'\n','歌词：','\n',format_lyric,'\n','-----------------------------')

       
