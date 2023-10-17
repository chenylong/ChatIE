import re

content = ('1、《中华人民共和国食品安全法》第一百二十六条第一款\u3000违反本法规定，有下列情形之一的，由县级以上人民政府食品安全监督管理部门责令改正，给予警告；拒不改正的，处五千元以上五万元以下罚款；情节严重的，责令停产停业，直至吊销许可证：\n    (一)食品、食品添加剂生产者未按规定对采购的食品原料和生产的食品、食品添加剂进行检验;\n    (二)食品生产经营企业未按规定建立食品安全管理制度，或者未按规定配备或者培训、考核食品安全管理人员;\n    (三)食品、食品添加剂生产经营者进货时未查验许可证和相关证明文件，或者未按规定建立并遵守进货查验记录、出厂检验记录和销售记录制度;\n     (七)食品经营者未按规定要求销售食品;\n '
           '\n2、《中华人民共和国食品安全法实施条例》第六十七条\u3000有下列情形之一的，属于食品安全法第一百二十三条至第一百二十六条、第一百三十二条以及本条例第七十二条、第七十三条规定的情节严重情形：\n\u3000\u3000（一）违法行为涉及的产品货值金额2万元以上或者违法行为持续时间3个月以上；\n\u3000\u3000（二）造成食源性疾病并出现死亡病例，或者造成30人以上食源性疾病但未出现死亡病例；')

content2 ="1、士大夫；\u3000违2、张\u3000瑟；"
pattern = re.compile('[1-9]、(.*[1-9]?)、')
pattern2 = re.compile('1、')
print(pattern.match('1、士大夫；2、张瑟；'))

content =content.strip('').strip('\n').strip('\r\n').replace(u'\u3000', u' ').replace(u'\xa0', u'')
content =content.replace('\n',' ')
print(content)


stra = pattern.match(content)
print(stra)

p3 = r'[1-9]、(.*)[1-9]、'

print(content2)
content2 = content2.replace(u'\u3000',u'')
print(content2)
match = re.search(p3,content)
if match:
    result = match.group(1)
    print("有匹配到 ",result)
else:
    print("未匹配")


liststr = content.split(r'[1-9]、')
print(liststr)


result = re.split(r'[1-9]、',content)
print(result)