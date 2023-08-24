import requests
API_URL = 'https://model-app-func-modelsc-bb-eaab-fulwbopjkp.cn-hangzhou.fcapp.run/invoke'
def post_request(url, json):
	with requests.Session() as session:
		response = session.post(url,json=json,)
		return response
payload = {"hello"}
response = post_request(API_URL, json=payload)
print("response:", response.json())