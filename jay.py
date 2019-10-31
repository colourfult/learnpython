import requests
res = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=70379103677690008&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
music = res.json()
music_list = music['data']['song']['list']
for music_name in music_list:
    song = music_name['name']
    zhuanji = music_name['album']['name']
    time = music_name['interval']
    url = 'https://y.qq.com/n/yqq/song/'+music_name['mid']+'.html'
    print('歌曲名：'+song+'，所属专辑：《'+zhuanji+'》，播放时长：'+str(time)+'秒','\n','播放链接：'+url)