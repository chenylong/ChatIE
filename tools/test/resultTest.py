#--coding:utf-8--
import json
import re
# from gradio_client import Client
#
# client = Client("http://model-ui-func.modelscope-d75fdbb4-60ba-418a-962e-6a0d4c2ece32.1569834201311714.cn-hangzhou.fc.devsapp.net/")
# content = '''今天星期几'''
#
# result = client.predict(
# 				content,	# str in 'text' Textbox component
# 				api_name="/predict"
# )
# print(result)

result ="{'Code': '200', 'Data': '今天星期几？', 'Message': '', 'RequestId': '1-652fb1df-f84967f762bb0e802bdbf32e', 'Success': 'True'}"

result2 = '''
{
	"Code": 200,
	"Data": "今填？",
	"Message": "",
	"RequestId": "1-652fb1df-f84967f762bb0e802bdbf32e",
	"Success": True
}
'''

content ="{ 'Data': '你是一个信息提取专家，已知监管事项拆解和生产的要求如下 一是为避免法律、行政法规和部门规章相关条款在实施依据中多次重复援引，事项名称原则上按法律、行政法规和部门规章的“条”或“款”的规定内容加以确定。 二是对“条”或“款”中罗列的多项具体违法情形，原则上不再拆分为多个事项；但罗列的违法情形涉及援引其他法律、行政法规和部门规章条款的，单独作为一个事项列出。 三是部门规章在法律、行政法规规定的给予行政处罚的行为、种类和幅度范围内作出的具 体规定，在实施依据中列出，不再另外单列事项。 四是同一法律、行政法规条款同时包含行政处罚、行政强制事项的，分别作为一个事项列出。 事项生成的名称要求如下： 一是行政处罚、行政强制事项名称，原则上根据设定该事项的法律、行政法规和部门规章条款内容进行概括提炼，统一规范为“对 XX 行为的行政处罚（行政强制）”。 二是部分涉及多种违法情形、难以概括提炼的，以罗列的多种违法情形中的第一项为代表，统一规范为“对 XX 等行为的行政处罚（行政强制）。 生成样例如下： （样例1）《中华人民共和国合伙企业法》第九十三条的内容为：违反本法规定，提交虚假文件或者采取其他欺骗手段，取得合伙企业登记的，由企业登记机关责令改正，处以五千元以上五万元以下的罚款；。 产生的事项为：对提交虚假文件或者采取其他欺骗手段，取得合伙企业登记的行政处罚，涉及的监管对象：合伙企业，涉及到的监管部门是：市场监管部门，检查内容：提交虚假文件或者采取其他欺骗手段，取得合伙企业登记； （样例2）《中华人民共和国合伙企业法》第九十四条的内容为：违反本法规定，合伙企业未在其名称中标明“普通合伙”、“特殊普通合伙”或者“有限合伙”字样的，由企业登记机关责令限期改正，处以二千元以上一万元以下的罚款。 产生的事项为：对合伙企业未在其名称中标明“普通合伙”、“特殊普通合伙”或者“有限合伙”字样的行政处罚，涉及的监管对象：合伙企业，涉及到的监管部门是：市场监管部门 ，检查内容：合伙企业未在其名称中标明“普通合伙”、“特殊普通合伙”或者“有限合伙”字样； （样例3）《浙江省食品小作坊小餐饮店小食杂店和食品摊贩管理规定》第十六条第二款\u3000食品小作坊、小餐饮店、小食杂店和食品摊贩应当在生产经营场所明显位置张挂登记证、登记卡和从业人员有效的健康证明，接受社会监督。产生的事项为：对小食杂店张挂登记证或者从业人员健康证明的行政检查；涉及的监管对象为：小食杂店，涉及到的监管部门是：市场监管部门，检查内容：登记证、登记卡和从业人员有效的健康证明是否在明显位置张挂； (样例4) 《麻醉药品和精神药品管理条例》第七十二条\u3000取得印鉴卡的医疗机构违反本条例的规定，有下列情形之一的，由设区的市级人民政府卫生主管部门责令限期改正，给予警告；逾期不改正的，处5000元以上1万元以下的罚款；情节严重的，吊销其印鉴卡；对直接负责的主管人员和其他直接责任人员，依法给予降级、撤职、开除的处分：（一）未依照规定购买、储存麻醉药品和第一类精神药品的；（二）未依照规定保存麻醉药品和精神药品专用处方，或者未依照规定进行处方专册登记的；（三）未依照规定报告麻醉药品和精神药品的进货、库存、使用数量的；\n产生的事项为：对取得印鉴卡的医疗机构未按规定购买、储存、保存、报告、备案、销毁麻醉药品和精神药品的行政处罚；涉及的监管对象为：取得印鉴卡的医疗机构，涉及到的检查部门是：卫生保健部门，检查内容：（一）未依照规定购买、储存麻醉药品和第一类精神药品的；（二）未依照规定保存麻醉药品和精神药品专用处方，或者未依照规定进行处方专册登记的；（三）未依照规定报告麻醉药品和精神药品的进货、库存、使用数量的。 根据上述监管事项的生成规则以及样例信息 请问 《杭州市燃气管理条例》第二十三条 在燃气设施保护范围内，从事敷设管道、打桩、顶进、挖掘、钻探等可能影响燃气设施安全活动的，建设单位应当委托具有相应施工资质的单位施工，会同燃气经营者制定燃气设施安全保护方案，签订安全监护协议书，并在施工中落实相应的安全保护措施。建设单位应当至少在开工前二十四小时书面通知燃气经营者，燃气经营者应当派专业人员到施工现场指导和监护。 因施工造成燃气设施损坏的，建设单位或者施工单位应当立即采取紧急保护措施，及时告知并协助燃气经营者进行抢修；造成损失的，应当依法承担相应责任。 可以生成的监管事项内容是什么？，若可以合并，请尽量合并，打印格式如下：事项名称1：XXXXXX，涉及的监管对象：XXXX，涉及的监管部门：XXXX，检查内容:XXX；如果有多个事项，请换行显示；若无法合并，请用多个A4纸，一题一行展示，例如 事项名称2：XXXXXX，涉及的监管对象：XXXX，涉及的监管部门：XXXX，检查内容:XXX。谢谢\n\n可以合并的事项名称1：在燃气设施保护范围内，从事敷设管道、打桩、顶进、挖掘、钻探等可能影响燃气设施安全活动的，建设单位应当委托具有相应施工资质的单位施工，会同燃气经营者制定燃气设施安全保护方案，签订安全监护协议书，并在施工中落实相应的安全保护措施，涉及的监管对象：建设单位和施工单位，涉及的监管部门：住建部门，检查内容：制定燃气设施安全保护方案，签订安全监护协议书，并在施工中落实相应的安全保护措施；若无法合并，请用多个A4纸，一题一行展示，例如 事项名称2：因施工造成燃气设施损坏的，建设单位或者施工单位应当立即采取紧急保护措施，及时告知并协助燃气经营者进行抢修；造成损失的，应当依法承担相应责任。 涉及的监管对象：建设单位和施工单位，涉及的监管部门：住建部门，检查内容：因施工造成燃气设施损坏的，建设单位或者施工单位应当立即采取紧急保护措施，及时告知并协助燃气经营者进行抢修。', , 'RequestId': '1-652fc600-611c923fd187dd1085d0efca', 'Success': 'True'}"
content =content.strip('').strip('\n').strip('\r\n').replace(u'\u3000', u' ').replace(u'\xa0', u'')
content =content.replace('\n',' ')
#js = json.loads(result)
result3 = content.replace("'",'"')
print(result3)
# result = json.loads(result3)
# print(result)

result2 = json.dumps(result2, ensure_ascii=False)
js = result

print(js)

print(type(result2),type(js))
# print(type(js),js["Data"],js["Success"])



content = '''你是一个信息提取专家，已知监管事项拆解和生产的要求如下 一是为避免法律、行政法规和部门规章相关条款在实施依据中多次重复援引，事项名称原则上按法律、行政法规和部门规章的“条”或“款”的规定内容加以确定。 二是对“条”或“款”中罗列的多项具体违法情形，原则上不再拆分为多个事项；但罗列的违法情形涉及援引其他法律、行政法规和部门规章条款的，单独作为一个事项列出。 三是部门规章在法律、行政法规规定的给予行政处罚的行为、种类和幅度范围内作出的具 体规定，在实施依据中列出，不再另外单列事项。 四是同一法律、行政法规条款同时包含行政处罚、行政强制事项的，分别作为一个事项列出。 事项生成的名称要求如下： 一是行政处罚、行政强制事项名称，原则上根据设定该事项的法律、行政法规和部门规章条款内容进行概括提炼，统一规范为“对 XX 行为的行政处罚（行政强制）”。 二是部分涉及多种违法情形、难以概括提炼的，以罗列的多种违法情形中的第一项为代表，统一规范为“对 XX 等行为的行政处罚（行政强制）。 生成样例如下： （样例1）《中华人民共和国合伙企业法》第九十三条的内容为：违反本法规定，提交虚假文件或者采取其他欺骗手段，取得合伙企业登记的，由企业登记机关责令改正，处以五千元以上五万元以下的罚款；。 产生的事项为：对提交虚假文件或者采取其他欺骗手段，取得合伙企业登记的行政处罚，涉及的监管对象：合伙企业，涉及到的监管部门是：市场监管部门，检查内容：提交虚假文件或者采取其他欺骗手段，取得合伙企业登记； （样例2）《中华人民共和国合伙企业法》第九十四条的内容为：违反本法规定，合伙企业未在其名称中标明“普通合伙”、“特殊普通合伙”或者“有限合伙”字样的，由企业登记机关责令限期改正，处以二千元以上一万元以下的罚款。 产生的事项为：对合伙企业未在其名称中标明“普通合伙”、“特殊普通合伙”或者“有限合伙”字样的行政处罚，涉及的监管对象：合伙企业，涉及到的监管部门是：市场监管部门 ，检查内容：合伙企业未在其名称中标明“普通合伙”、“特殊普通合伙”或者“有限合伙”字样； （样例3）《浙江省食品小作坊小餐饮店小食杂店和食品摊贩管理规定》第十六条第二款　食品小作坊、小餐饮店、小食杂店和食品摊贩应当在生产经营场所明显位置张挂登记证、登记卡和从业人员有效的健康证明，接受社会监督。产生的事项为：对小食杂店张挂登记证或者从业人员健康证明的行政检查；涉及的监管对象为：小食杂店，涉及到的监管部门是：市场监管部门，检查内容：登记证、登记卡和从业人员有效的健康证明是否在明显位置张挂； (样例4) 《麻醉药品和精神药品管理条例》第七十二条　取得印鉴卡的医疗机构违反本条例的规定，有下列情形之一的，由设区的市级人民政府卫生主管部门责令限期改正，给予警告；逾期不改正的，处5000元以上1万元以下的罚款；情节严重的，吊销其印鉴卡；对直接负责的主管人员和其他直接责任人员，依法给予降级、撤职、开除的处分：（一）未依照规定购买、储存麻醉药品和第一类精神药品的；（二）未依照规定保存麻醉药品和精神药品专用处方，或者未依照规定进行处方专册登记的；（三）未依照规定报告麻醉药品和精神药品的进货、库存、使用数量的；产生的事项为：对取得印鉴卡的医疗机构未按规定购买、储存、保存、报告、备案、销毁麻醉药品和精神药品的行政处罚；涉及的监管对象为：取得印鉴卡的医疗机构，涉及到的检查部门是：卫生保健部门，检查内容：（一）未依照规定购买、储存麻醉药品和第一类精神药品的；（二）未依照规定保存麻醉药品和精神药品专用处方，或者未依照规定进行处方专册登记的；（三）未依照规定报告麻醉药品和精神药品的进货、库存、使用数量的。 根据上述监管事项的生成规则以及样例信息 请问 《杭州市燃气管理条例》第二十三条 在燃气设施保护范围内，从事敷设管道、打桩、顶进、挖掘、钻探等可能影响燃气设施安全活动的，建设单位应当委托具有相应施工资质的单位施工，会同燃气经营者制定燃气设施安全保护方案，签订安全监护协议书，并在施工中落实相应的安全保护措施。建设单位应当至少在开工前二十四小时书面通知燃气经营者，燃气经营者应当派专业人员到施工现场指导和监护。 因施工造成燃气设施损坏的，建设单位或者施工单位应当立即采取紧急保护措施，及时告知并协助燃气经营者进行抢修；造成损失的，应当依法承担相应责任。可以生成的监管事项内容是什么？，若监管事项可以合并，请尽量合并，数据输出格式如下：事项名称1：XXXXXX，涉及的监管对象：XXXX，涉及的监管部门：XXXX，检查内容:XXX；如果有多个事项，请换行显示；'''

print(content)


content = "{ 'Data': '\n\n监管事项生成的名称要求如下：一是行政处罚、行政强制事项名称，原则上根据设定该事项的法律、行政法规和部门规章条款内容进行概括提炼，统一规范为“对XX行为的行政处罚（行政强制）”。二是部分涉及多种违法情形、难以概括提炼的，以罗列的多种违法情形中的第一项为代表，统一规范为“对XX等行为的行政处罚（行政强制）。 根据上述监管事项的生成规则以及样例信息《杭州市燃气管理条例》第二十三条 在燃气设施保护范围内，从事敷设管道、打桩、顶进、挖掘、钻探等可能影响燃气设施安全活动的，建设单位应当委托具有相应施工资质的单位施工，会同燃气经营者制定燃气设施安全保护方案，签订安全监护协议书，并在施工中落实相应的安全保护措施。建设单位应当至少在开工前二十四小时书面通知燃气经营者，燃气经营者应当派专业人员到施工现场指导和监护。 因施工造成燃气设施损坏的，建设单位或者施工单位应当立即采取紧急保护措施，及时告知并协助燃气经营者进行抢修；造成损失的，应当依法承担相应责任。 可以生成的监管事项内容是什么？ 事项名称1：对燃气设施保护范围内可能影响燃气设施安全活动的建设单位未委托具有相应施工资质的单位施工或者未采取相应安全保护措施的行政处罚，涉及的监管对象为燃气设施保护范围内可能影响燃气设施安全活动的建设单位，涉及的监管部门为燃气管理部门，检查内容：未委托具有相应施工资质的单位施工或者未采取相应安全保护措施；事项名称2：对燃气设施保护范围内可能影响燃气设施安全活动的建设单位未与燃气经营者签订安全监护协议书或者燃气经营者未派专业人员到施工现场指导和监护的行政处罚，涉及的监管对象为燃气设施保护范围内可能影响燃气设施安全活动的建设单位，涉及的监管部门为燃气管理部门，检查内容：未签订安全监护协议书或者燃气经营者未派专业人员到施工现场指导和监护；事项名称3：对燃气设施保护范围内可能影响燃气设施安全活动的建设单位因施工造成燃气设施损坏未立即采取紧急保护措施或者未告知并协助燃气经营者进行抢修的行政处罚，涉及的监管对象为燃气设施保护范围内可能影响燃气设施安全活动的建设单位，涉及的监管部门为燃气管理部门，检查内容：未立即采取紧急保护措施或者未告知并协助燃气经营者进行抢', , 'RequestId': '1-652fcd6a-087c373c3d34de4e5bb54a00', 'Success': 'True'}"


p3 = r'？ 事项名称1(.*)RequestId'
match = re.search(p3,content)
if match:
    result = match.group(0)
    print("有匹配到 ",result)
else:
    print("未匹配")
