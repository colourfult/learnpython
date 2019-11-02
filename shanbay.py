import requests
import time
shengci = {}
wrong = []
wrong_dict = {}
right = []
level = []
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
try:
    for i in range(len(fanwei1)):
        #print(str(i+1)+'、'+fanwei1[i][1])
        level1 =str(i+1)+'、'+fanwei1[i][1]  
        level.append(level1)  #将测试水平存入列表以实现横向输出
    print('  '.join(level))  #将列表转换为字符串
    choice = int(input())
    url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
    params = {
    'category': fanwei1[choice][0],
'_': '1572593390674',
}
    res1 = requests.get(url,params=params,headers=headers)
    words = res1.json()
    words_list = words['data'] #在json中找到单词列表
    print('下面的单词您认识么？0--认识，1--不认识')
    #for x in range(5):
    for x in range(len(words_list)): #遍历单词列表，根据单词数量确定循环次数
        word2 = words_list[x]
        word = word2['content']  #获取单词
        rank = word2['rank']  #获取单词rank值
        trans = word2['definition_choices'] #获取单词解释列表
        print('第'+str(x+1)+'个 / 共'+str(len(words_list))+'个 （0--认识，1--不认识） ：'+word)
        choice1 = int(input())
        if choice1 == 1:
            for c in range(len(trans)): #遍历单词解释列表
                rank1 = trans[c]['rank']  #获取单词列表rank值
                word_trans = trans[c]['definition']
                if rank == rank1:  #判断如果单词的rank值和列表中某个单词的rank值相等，那么这个解释就是该单词的解释
                    shengci[word] = word_trans
        else:
            print('请选择 '+word+' 的意思：')
            for b in range(len(trans)):
                trans1 = trans[b]['definition'] #遍历打印单词解释
                print(str(b+1)+'、'+trans1)
            choice2 = int(input())
            trans2 = trans[choice2-1]['rank'] # 定义选择的单词的rank值
            trans3 = trans[choice2-1]['definition'] #定义选择的单词的翻译
            if rank == trans2:  #将单词正确翻译的rank值与选择的翻译rank值对比来确定是否回答正确
                print('回答正确')
                right.append(word)
            else:
                wrong.append(word)
                print('回答错误')
                wrong_dict[word] = trans3 #将错误的单词及翻译存入字典
        if x == len(words_list)-1:
            print('--------------','\n','答题结束','\n','')        

    if len(shengci) and len(wrong_dict) :
        print('不认识的单词有：','\n','')
        for key,value in shengci.items():
            print(key+'--'+value)
        print('','\n','---------------------------------','\n','')
        print('回答错误的单词有：','\n','')
    #print('回答错误的单词有：')
    #print('、'.join(wrong))#将列表转换为字符串
    #print('')
        for key1,value1 in wrong_dict.items():
            print(key1+'--'+value1)
    elif len(shengci) == False and len(wrong_dict) :
        print('回答错误的单词有：','\n','')
        for key,value in wrong_dict.items():
            print(key+'--'+value)
    elif len(shengci)  and len(wrong_dict) == False:
        print('不认识的单词有：','\n','')
        for key,value in shengci.items():
            print(key+'--'+value)
    else:
        print('恭喜你词汇量惊人，认识本次出示的所有'+fanwei1[choice-1][0]+'词汇！！')
    time.sleep(2)
    print('','\n','---------------------------------','\n','','\n','本次测试结束，感谢使用！')
except:
    print('您的输入有误，程序自动退出，请重新运行。')
    pass
