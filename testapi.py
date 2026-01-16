import requests

url = "http://127.0.0.1:5000/predict"

data = {
  'Age': 60,
  'Account_Manager': 1,
  'Years': 2,
  'Num_Sites': 2
}

response = requests.post(url, data=data) 
print(response.json())