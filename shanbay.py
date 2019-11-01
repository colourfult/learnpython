import requests
shengci = {}
cuoti = []
url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
params = {
    '_': '1572592534813',
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
}
res = requests.get(url,params=params,headers=headers)
fanwei = res.json()
fanwei1 = fanwei['data']
print('请选择您要测试的类型：')
for i in range(len(fanwei1)):
    print(str(i+1)+'、'+fanwei1[i][1])
choice = int(input())
url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
params = {
    'category': fanwei1[choice][0],
'_': '1572593390674',
}
res1 = requests.get(url,params=params,headers=headers)
words = res1.json()
words_list = words['data']
print('下面的单词您认识么？0--认识，1--不认识')
for x in range(5):
#for x in range(len(words_list)):
    word2 = words_list[x]
    word = word2['content']
    rank = word2['rank']
    print('第'+str(x+1)+'个 / 共'+str(len(words_list))+'个  ：'+word)
    choice1 = int(input())
    if choice1 == 1:
        shengci[word]:'1'
    else:
        print('请选择 '+word+' 的意思：')
        trans = word2['definition_choices']
        for b in range(len(trans)):
            trans1 = trans[b]['definition']
            print(str(b+1)+'、'+trans1)
        choice2 = int(input())
        trans2 = trans[choice2-1]['rank']
        if rank == trans2:
            print('回答正确')
        else:
            cuoti.append(word)
            print('回答错误')
    print('下一题（0--认识，1--不认识）','\n','--------------')
buhui = filter(lambda x:'1'==x[1], shengci.items())
for(key,value) in buhui:
    print(key)
print('回答错误的单词有：')
print('、'.join(cuoti))#将列表转换为字符串
    
