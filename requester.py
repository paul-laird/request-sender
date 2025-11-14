url = 'https://helloworld.requestcatcher.com/test'
data = 'Hello World!'

for i in range(10000):
  resp = requests.post(url, data=data + str(i))
  time.sleep(15)
  print(f"Status Code: {resp.status_code}")
  print(f"Response Text: {resp.text}")
