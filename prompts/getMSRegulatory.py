# coding=utf8
import os
import pymysql
import json
import re

def data2Prompt(cursor,sql,filename):
    if sql is None or sql == '':
        sql = "select version()"
    else:
        sql = sql

    cursor.execute(sql)
    results = cursor.fetchall()  # 获取所有查询结果

    # 文化模板
    # 前缀
    sx_gz = "你是一个信息提取专家，已知监管事项拆解和生产的要求如下 一是为避免法律、行政法规和部门规章相关条款在实施依据中多次重复援引，事项名称原则上按法律、行政法规和部门规章的“条”或“款”的规定内容加以确定。 二是对“条”或“款”中罗列的多项具体违法情形，原则上不再拆分为多个事项；但罗列的违法情形涉及援引其他法律、行政法规和部门规章条款的，单独作为一个事项列出。 三是部门规章在法律、行政法规规定的给予行政处罚的行为、种类和幅度范围内作出的具 体规定，在实施依据中列出，不再另外单列事项。 四是同一法律、行政法规条款同时包含行政处罚、行政强制事项的，分别作为一个事项列出。 事项生成的名称要求如下： 一是行政处罚、行政强制事项名称，原则上根据设定该事项的法律、行政法规和部门规章条款内容进行概括提炼，统一规范为“对 XX 行为的行政处罚（行政强制）”。 二是部分涉及多种违法情形、难以概括提炼的，以罗列的多种违法情形中的第一项为代表，统一规范为“对 XX 等行为的行政处罚（行政强制）。"
    sx_tj = "根据已知的监管事项的拆解要求和命名规范，请问 "
    sx_sc = " 该条法律法规可以生成的监管事项内容是什么？，若可以生成多条事项，请尽量合并，输出格式如下：事项名称1：XXXXXX，涉及的监管对象：XXXX，涉及的监管部门：XXXX，检查内容:XXX；如果有多个事项，请换行显示。"
    x=0

    file = open(filename, 'a+', encoding='utf-8')

    for row in results:
        # 处理查询结果
        #print(row) list_name ,regulatory_obj ,line_name ,basis

        #basis 可能有多个处罚依据，进行拆分，一个处罚依据一个事项
        content = row[3]
        content = content.strip('').strip('\n').strip('\r\n').replace(u'\u3000', u' ').replace(u'\xa0', u'')
        content = content.replace('\n', ' ')

        pattern = re.compile('1、')
        match = re.search(pattern, content)
        #strProment = ""
        x = x +1
        if match: #是多组处罚依据，分开打印
            result = re.split(r'[1-9]、', content) #根据正则表达式 分割
            i = 0
            for li in result:

                if li == '':
                    i=i+1
                    continue

                else:
                    i = i + 1
                    # strProment = str(li) + "\n 产生的事项为："+row[0]+"；涉及的监管对象为："+row[1]+"涉及到的检查部门是："+row[2]
                    # print('#-- start -- #',x ,'条 ，',i,' 个 ', row[0])
                    # print(strProment)
                    # print('#-- end -- #')
                    jsconte = {"instruction": '' + sx_gz + sx_tj + str(li) + sx_sc,
                               "input": "",
                               "output": "根据以上信息，该条法律法规产生的事项为，事项名称1："+row[0]+"；涉及的监管对象为："+row[1]+"；涉及到的检查部门是："+row[2]+"。"
                               }
                    print('#-- start -- #', x, '条 ，', i, ' 个 ', row[0])
                    print(jsconte)
                    print(sx_gz + sx_tj + str(li) + sx_sc)
                    print('#-- end -- #')
                    file.write(json.dumps(jsconte, ensure_ascii=False) + ',\n')


        else:
            # strProment = row[3] + "\n 产生的事项为：" + row[0] + "；涉及的监管对象为：" + row[1] + "涉及到的检查部门是：" + \
            #              row[2]
            # print('#-- start -- #',x ,'条 ，', row[0])
            # print(strProment)
            # print('#-- end -- #')

            jsconte = {"instruction": '' + sx_gz + sx_tj + content  + sx_sc,
                       "input": "",
                       "output": "根据以上信息，该条法律法规产生的事项为，事项名称1：" + row[0] + "；涉及的监管对象为：" + row[
                           1] + "；涉及到的检查部门是：" + row[2] + "。"
                       }
            print('#-- start -- #',x ,'条 ，', row[0])
            print(jsconte)
            print(sx_gz + sx_tj + content  + sx_sc)
            print('#-- end -- #')
            file.write(json.dumps(jsconte, ensure_ascii=False) + ',\n')

    file.close()




if __name__ == '__main__':

    connection = pymysql.connect(
        host='localhost',  # MySQL服务器主机名
        user='root',  # MySQL用户名
        password='chen',  # MySQL密码
        database='test'  # 要连接的数据库名称
    )

    cursor = connection.cursor()

    line_name = '市场监管'
    querySql = ("select distinct list_name ,regulatory_obj ,line_name ,basis  from "
                "v_regulatory_list vrl where line_name like '%"+line_name+"%' "
                "and created_dept_name  like '%浙江%' "
                )
    print('start chaxun ')

    filename = 'E:/py/ChatIE/prompts/prompt_law/RE/' + line_name + '.json'
    if os.path.exists(filename):
        print(filename,' 已经存在了')
    else:
        print(filename, ' 去生成')
        data2Prompt(cursor, querySql,filename)

    cursor.close()
    connection.close()


