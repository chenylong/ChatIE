import pymysql
import re
connection = pymysql.connect(
    host='localhost',  # MySQL服务器主机名
    user='root',  # MySQL用户名
    password='chen',  # MySQL密码
    database='test'  # 要连接的数据库名称
)


def data2Prompt(cursor,sql):
    if sql is None or sql == '':
        sql = "select version()"
    else:
        sql = sql

    cursor.execute(sql)
    results = cursor.fetchall()  # 获取所有查询结果

    x=0
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
                    strProment = str(li) + "\n 产生的事项为："+row[0]+"；涉及的监管对象为："+row[1]+"涉及到的检查部门是："+row[2]
                    print('#-- start -- #',x ,'条 ，',i,' 个 ', row[0])
                    print(strProment)
                    print('#-- end -- #')
        else:
            strProment = row[3] + "\n 产生的事项为：" + row[0] + "；涉及的监管对象为：" + row[1] + "涉及到的检查部门是：" + \
                         row[2]
            print('#-- start -- #',x ,'条 ，', row[0])
            print(strProment)
            print('#-- end -- #')






if __name__ == '__main__':
    cursor = connection.cursor()
    querySql = ("select distinct list_name ,regulatory_obj ,line_name ,basis  from "
                "v_regulatory_list vrl where line_name like '%卫生%' "
               "and created_dept_name  like '%浙江%' "
              #  " and list_name   like '%对电子商务经营者履行销售商品或提供服务的检查监控和知识产权保护义务、保障消费者合法权益的行政检查%'"
              #  " limit 10 "
                )
    data2Prompt(cursor,querySql)

    cursor.close()
    connection.close()