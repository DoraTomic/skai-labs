import requests

BASE = "http://127.0.0.1:5000/"

request = {
  "start_times": [10, 20, 30, 40, 50, 60],
  "end_times": [15, 25, 35, 45, 55, 65]
}

responce = requests.post(BASE + "interviewscheduler", json=request)
print(responce.json())