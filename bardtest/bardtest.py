
from bardapi import Bard
import os

os.environ["_BARD_API_KEY"] = "bgjc7Dje3NJ_0UA75HlZz-D_ixtm3RM2C3ZohMCdHBCojCRo4HnLtr1muKr0mhVG67xG4w."
token = 'bgjc7Dje3NJ_0UA75HlZz-D_ixtm3RM2C3ZohMCdHBCojCRo4HnLtr1muKr0mhVG67xG4w.'
#message = input("输入内容：")
message = input("qingshuru :")
messages = Bard().get_answer(str(message))['content']

print(messages)
# Example:
#         >>> token = 'xxxxxx'
#         >>> bard = Bard(token=token)
#
#         >>> response = bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")
#         >>> print(response['content'])
#
#         >>> response = bard.get_answer("Show me grocery stores close to the entrance to Grand Teton National Park and give me ideas for good snacks to bring hiking", tool=Tool.GOOGLE_MAPS)
#         >>> print(response['content'])

# token = 'bgjc7Dje3NJ_0UA75HlZz-D_ixtm3RM2C3ZohMCdHBCojCRo4HnLtr1muKr0mhVG67xG4w.'
# bard = Bard(token=token)
# response = Bard.get_answer("Show me grocery stores close to the entrance to Grand Teton National Park and give me ideas for good snacks to bring hiking")
# print(response['content'])
