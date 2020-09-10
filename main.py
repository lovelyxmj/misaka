import sql
import requests
import json
import re
from urllib import parse
import update
#导入库


def AddSQL(uname,ulevel,usign,umid,upic,yubanid):
    sqlstr = str(sql.queries(f'SELECT umid FROM nodes WHERE umid="{umid}"'))
    if str(umid) in sqlstr:
        return('')
    else:
        SQLcode1 = f'INSERT INTO nodes (uname,ulevel,usign,umid,upic,yubanid) VALUES ("{uname}","{ulevel}","{usign}","{umid}","{upic}","{yubanid}");'
        sql.write(SQLcode1)
#定义可以快捷插入行的函数
    
sql.write(f'DELETE FROM nodes;')#清空数据表
print('清空数据表ing')

def GetData(search):
    GetMaxPages = requests.get(f'https://api.bilibili.com/x/web-interface/search/type?keyword={search}&search_type=bili_user&page=1')
    MaxPages = json.loads(GetMaxPages.text)['data']['numPages']#获取总页码

    for i in range(1,int(MaxPages)+1):  #让for循环的i从1开始
        print(f'尝试刷新页面为{i}的数据')
        GetUserDataUri = f'https://api.bilibili.com/x/web-interface/search/type?keyword={search}&search_type=bili_user&page={i}'
        #拼接请求的uri
        GetUserHttp = requests.get(GetUserDataUri)
        jsondata = json.loads(GetUserHttp.text) #将str转换为json（b站返回是str）
        UserNumber = len(jsondata['data']['result'])#获得本页用户数量
        print(f'本页共找到{UserNumber}个用户')

        #开始获得用户信息
        for i in range(UserNumber):

            #uname：用户名
            #ulevel：用户等级
            #usign：用户签名
            #umid：用户在bilibili的唯一id
            #upic：用户的头像URL

            UserData = jsondata['data']['result'][i]
            uname = UserData['uname']
            ulevel = UserData['level']
            usign = UserData['usign'].replace('"','') #解决签名内的引号会干扰程序
            umid = UserData['mid']
            upic = UserData['upic']
        
            #提取用户名中的数字以获得御坂妹ID 比如这样的“御坂妹10042号”→10042
            try:
                yubanid = re.findall("\d+",uname.replace('O','0').replace('o','0').replace('-',''))[0]#解决有用户使用O或者o代替0
            except IndexError:
                print(f'用户{uname}未连接御坂网络')
                continue

            yubanid = yubanid.zfill(5)#当数字位数不够时补上
            print(f'发现御坂网络节点{uname}')
            AddSQL(uname,ulevel,usign,umid,upic,yubanid)#加入数据库


search_list = ['御坂','御坂妹']
for i in range(len(search_list)):
    GetData(parse.quote(search_list[i]))