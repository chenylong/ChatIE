# coding=utf8
import requests
from gradio_client import Client

def ty_request():
	API_URL = 'https://model-app-func-modelsc-bb-eaab-fulwbopjkp.cn-hangzhou.fcapp.run/invoke'
	def post_request(url, json):
		with requests.Session() as session:
			response = session.post(url,json=json,)
			return response
	payload = {"hello"}
	response = post_request(API_URL, json=payload)
	print("response:", response.json())
	return response

def ty_gradio(mess):
	client = Client(
		"http://model-ui-func.modelscope-ddaed09f-d8a8-4275-b4b8-eaa0b4484292.1569834201311714.cn-hangzhou.fc.devsapp.net/")

	result = client.predict(
		mess,  # str in 'Message' Textbox component
		api_name="/chat"
	)
	print(result)
	return result

def zw_request(mess):
	API_URL = 'http://192.168.1.169:8005/nlpsearch'
	def post_request(url, json):
		with requests.Session() as session:
			response = session.post(url,json=json,)
			return response

	payload = {
		"scene": "legal_advice",
		"text": mess
	}
	response = post_request(API_URL, json=payload)
	print("response:", response.json())
	return response

if __name__ == "__main__":
	#ty_gradio("杭州的旅游攻略")
	response = zw_request("强奸犯的量刑原则")
	rjson = response.json()
	print(rjson["data"]["answer"])

