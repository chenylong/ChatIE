# coding=utf-8
import json
import random
import ast
from gradio_client import Client


df_access = [
    ('@gYaKlfLGewYYkmZb7T3BlbkFJouvA5wegTYHbPcgWgI4D', 'sk-1Ni')
]

df_ret = {

    # 'chinese': {'所属专辑': ['歌曲', '音乐专辑'], '成立日期': ['机构', 'Date'], '海拔': ['地点', 'Number'],
    #             '官方语言': ['国家', '语言'], '占地面积': ['机构', 'Number'], '父亲': ['人物', '人物'],
    #             '歌手': ['歌曲', '人物'], '制片人': ['影视作品', '人物'], '导演': ['影视作品', '人物'],
    #             '首都': ['国家', '城市'], '主演': ['影视作品', '人物'], '董事长': ['企业', '人物'],
    #             '祖籍': ['人物', '地点'],
    #             '妻子': ['人物', '人物'], '母亲': ['人物', '人物'], '气候': ['行政区', '气候'],
    #             '面积': ['行政区', 'Number'], '主角': ['文学作品', '人物'], '邮政编码': ['行政区', 'Text'],
    #             '简称': ['机构', 'Text'],
    #             '出品公司': ['影视作品', '企业'], '注册资本': ['企业', 'Number'], '编剧': ['影视作品', '人物'],
    #             '创始人': ['企业', '人物'], '毕业院校': ['人物', '学校'], '国籍': ['人物', '国家'],
    #             '专业代码': ['学科专业', 'Text'], '朝代': ['历史人物', 'Text'], '作者': ['图书作品', '人物'],
    #             '作词': ['歌曲', '人物'], '所在城市': ['景点', '城市'], '嘉宾': ['电视综艺', '人物'],
    #             '总部地点': ['企业', '地点'],
    #             '人口数量': ['行政区', 'Number'], '代言人': ['企业/品牌', '人物'], '改编自': ['影视作品', '作品'],
    #             '校长': ['学校', '人物'], '丈夫': ['人物', '人物'], '主持人': ['电视综艺', '人物'],
    #             '主题曲': ['影视作品', '歌曲'],
    #             '修业年限': ['学科专业', 'Number'], '作曲': ['歌曲', '人物'], '号': ['历史人物', 'Text'],
    #             '上映时间': ['影视作品', 'Date'], '票房': ['影视作品', 'Number'], '饰演': ['娱乐人物', '人物'],
    #             '配音': ['娱乐人物', '人物'], '获奖': ['娱乐人物', '奖项']
    #             }

    'chinese': {
        '制定': ['机关名称', '法律法规名称'],
        '修改': ['机关名称', '法律法规名称'],
        '废止': ['机关名称', '法律法规名称'],
        '发布': ['机关名称', '法律法规名称'],
        '适用地区': ['法律法规名称', '地区名称'],
        '适用主体': ['法律法规名称', '主体名称'],
        '修订日期': ['法律法规名称', '具体日期'],
        '废止日期': ['法律法规名称', '具体日期'],
        '公布日期': ['法律法规名称', '具体日期'],
        '施行日期': ['法律法规名称', '具体日期'],
        '法律效力位阶': ['法律法规名称', '位阶名称'],
        '时效性': ['法律法规名称', '是否有效']
    }
}
re_s1_p_ty = {
    'chinese': '''给定的句子为："{}"\n\n给定关系列表：{}\n\n在给定的句子中，可能包含了给定关系列表中的哪些关系，请按照元组形式回复，多个关系之间用中文逗号'，'分割，如 (成立日期:[企业名称, 具体日期])， (法定代表人:[企业名称, 人名])。\n\n如果不存在则回答：无\n''',
}


def chat_re(inda, chatbot):
    print("---RE---")
    # mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    mess = ''
    typelist = inda['type']
    sent = inda['sentence']
    lang = inda['lang']

    out = []  # 输出列表 [(e1,r1,e2)]

    try:
        print('-----stage1---')
        stage1_tl = typelist
        s1p = re_s1_p_ty[lang].format(sent, str(stage1_tl))  #换成 re_s1_p_ty 话术试试
        print('组装后，prompt对应的内容为：',s1p)
        # mess.append({"role": "user", "content": s1p})
        mess = s1p
        print("调用qy模型，参数",mess)
        text1 = chatbot(mess)
        # mess.append({"role": "assistant", "content": text1})
        print("调用qy模型，反馈结果：")
        print(text1)

        # 正则提取结果
        # res1 = re.findall(r'\(.*?\)', text1)

        res1 = text1.split('：')[1].strip()
        print(res1)
        if res1 != []:
            # rels = [temp[1:-1].split(',') for temp in res1]
            # rels = list(set([re.sub('[\'"]', '', j).strip() for i in rels for j in i]))
            if res1.find('；') != -1:
                rels = res1.split('；')
            elif res1.find('、') != -1:
                rels = res1.split('、')
            elif res1.find('，') != -1:
                rels = res1.split('，')
            else:
                print("res1 格式有问题，无法拆分")

            for li in rels:
                # out = [('滴答', '歌手', '陈思成'), ('兰花指', '歌手', '阿里郎'), ('滴答', '歌手', '张碧晨')]
                # 当前结果是 制定（国务院，国内水路运输管理条例）、修改（国务院，国内水路运输管理条例） 需要进行格式化 输出列表 [(e1,r1,e2)]
                r1 = li.split('（')[0].strip()
                e1 = li.split('（')[1].split('，')[0]
                e2 = li.split('（')[1].split('，')[1]
                e2 = e2.split('）')[0]
                ru = (e1, r1, e2)
                out.append(ru)

        else:  # 说明正则没提取到，可能是单个类型的情况
            text1 = text1.strip().rstrip('、')
            rels = [text1]
        print("最终的rels:", rels)

    except Exception as e:
        print(e)
        print('re stage 1 none out or error')
        return ['error-stage1:' + str(e)], mess

    # print(mess)
    # out = [('滴答', '歌手', '陈思成'), ('兰花指', '歌手', '阿里郎'), ('滴答', '歌手', '张碧晨')]

    return out, mess

def chat(mess):
    print(" tiaozheng qytw ")
    # responde = create(
    #     model="gpt-3.5-turbo",
    #     messages=mess
    # )
    client = Client(
        "http://model-ui-func.modelscope-ddaed09f-d8a8-4275-b4b8-eaa0b4484292.1569834201311714.cn-hangzhou.fc.devsapp.net/")

    result = client.predict(
        mess,  # str in 'Message' Textbox component
        api_name="/chat"
    )

    # res = responde['choices'][0]['message']['content']
    res = result
    return res

def chatie(input_data):
    print('input data type:{}'.format(type(input_data)))
    print('input data:{}'.format(input_data))

    # 参数处理，默认参数
    task = input_data['task']
    lang = input_data['lang']
    typelist = input_data['type']
    access = input_data['access']

    ## account
    if access == "":
        print('using default access token')
        # tempes = random.choice(df_access)
        # input_data['access'] = tempes[1] + tempes[0][1:]

    ## chatgpt
    try:
        # openai.api_key = input_data['access']
        chatbot = chat
    except Exception as e:
        print('---chatbot---')
        print(e)
        input_data['result'] = ['error-chatbot']
        return input_data  # 没必要进行下去

    ## typelist, 空或者出错就用默认的
    try:
        typelist = ast.literal_eval(typelist)
        input_data['type'] = typelist
    except Exception as e:
        print('---typelist---')
        print(e)
        print(typelist)
        print('using default typelist')
        if task == 'RE':
            typelist = df_ret[lang]
            input_data['type'] = typelist

    # get output from chatgpt
    if task == 'RE':
        input_data['result'], input_data['mess'] = chat_re(input_data, chatbot)
        print(input_data)
    with open('access_record.json', 'a',encoding='utf-8') as fw:
        fw.write(json.dumps(input_data, ensure_ascii=False)+'\n')
    return input_data


if __name__ == "__main__":
    #p = '''第五部：《如懿传》是一部古装宫廷情感电视剧，由汪俊执导，周迅、霍建华、张钧甯、董洁、辛芷蕾、童瑶、李纯、邬君梅等主演'''
    p = '''国务院2023年7月20日修订了《国内水路运输管理条例》'''

    ind = {
        "sentence": p,
        "type": "",
        "access": "",
        "task": "RE",
        "lang": "chinese",

    }
    post_data = chatie(ind)
    print(post_data)
