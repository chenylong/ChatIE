import requests
API_URL = 'https://model-app-func-modelsce-adcece-ioluynujeu.cn-hangzhou.fcapp.run/invoke'
def post_request(url, json):
	with requests.Session() as session:
		response = session.post(url,json=json,)
		return response

content = "麻醉药品和精神药品管理条例》第七十二条的内容是什么"
payload = {"input": content}
response = post_request(API_URL, json=payload)
print("response:", response.json())

# payload = {"input": "蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是"}
# response = post_request(API_URL, json=payload)
# print("response:", response.json())