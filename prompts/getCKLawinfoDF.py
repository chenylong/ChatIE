# coding=utf8
import os
from time import sleep

from  clickhouse_driver import Client
import json

def getPromptLawJson(client,law_name,law_id,filename):
    #law_name = '浙江省测绘地理信息条例' #'中华人民共和国广告法'
    #law_id = 'MmM5MGU1YmI2YTI5MWY4NjAxNmE0Y2JkMDc4MjAyZjQ%3D' #'ZmY4MDgxODE3YWIyMzFlYjAxN2FiZDZiZDg2MDA1MmQ%3D'


    querySql= ("select a.*,b.num zhang,c.num tiao   from (select name_fa ,name_zhang,replaceOne(replaceOne(name_zhang,'第',''),'章','') zhangnum ,name_tiao,replaceOne(replaceOne(name_tiao,'第',''),'条','') tiaonum,"
               "groupArray(distinct content) as content"
               " from ods_law_provision olp   where name_fa  = '"+law_name+"'and law_id  = '"+law_id+"' and olp.name_kuan = 'None' "
                "group by name_fa,name_zhang,name_tiao"
                ") a left join dic_num b on ifNull(a.zhangnum,'') = b.code "
                "left join dic_num c on ifNull(a.tiaonum,'') = c.code"
                 " where  a.name_tiao <> '' and a.name_tiao <> 'None'  and a.name_tiao is not null "
                "order by  zhang, tiao  asc"
               )
    result = client.execute(querySql)
    for row in result:
        name_fa = row[0]
        name_tiao = row[3]
        name_content = row[5]
        str_content = ''.join(name_content)

        #根据提问词生成 prompt
          #   格式[{
          #   "instruction": "你是谁?",
          #   "input": "",
          #   "output": "我是Gitclone, 一个语言模型, 由来自git-cloner的研究人员训练。"
          # }，{},......]
        # 问话形式有
        first_qe_list = ('请问','请查询','查询','我想查询','我想知道','帮我查询一下',
    '帮我查询','你知道','你了解','你去查一下','你查一下','你查询一下')

        law_name_re1 = name_fa.replace('中华人民共和国','')
        law_name_re2= '我国'+law_name_re1

        #法律的别称list
        law_name_list = (name_fa,law_name_re1,law_name_re2)

        #问法list
        law_qe_list = ('的内容是什么？','有什么内容？','是什么样的？','包含什么内容？','都有什么内容?','涉及哪些方面?')

        #instruction 组合
        # output 组合
        file =  open(filename, 'a+', encoding='utf-8')
        for fq in first_qe_list:
            for ll in law_name_list:
                for lql in law_qe_list:
                    jsconte = {"instruction":''+fq+ll+name_tiao+lql,
                          "input": "",
                          "output":str_content
                          }
                    file.write(json.dumps(jsconte, ensure_ascii=False) + ',\n')
        file.close()
        print(name_fa,name_tiao,str_content)

if __name__ == '__main__':
    client = Client('192.168.1.142', user='ck', password='Eitmpou9', database='model', port=9000,settings={'send_receive_timeout': 3000000})
    client2 = Client('192.168.1.142', user='ck', password='Eitmpou9', database='model', port=9000,settings={'send_receive_timeout': 3000000})

    querySql = (
                "SELECT title ,law_id   from ods_law_base_info olbi where status ='1' and olbi.law_type  = '地方性法规' and  multiSearchAny(office,['浙江','杭州','宁波','温州','湖州','嘉兴','绍兴','金华','衢州','台州','丽水','舟山']) > 0"
                )
    result = client.execute(querySql)

    for row in result:
        law_name = row[0]
        law_id = row[1]
        filename = 'E:/py/ChatIE/prompts/DF/' + law_name + '.json'
        if os.path.exists(filename):
            print(filename,' 已经存在了')
        else:
            print(row)
            getPromptLawJson(client2,law_name,law_id,filename)