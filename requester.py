import requests
import time
url = 'https://helloworld.requestcatcher.com/test'
data = 'Hello World!'

with open('/var/www/html/request.log','w') as f:
  for i in range(10000):
    resp = requests.post(url, data=data + str(i))
    time.sleep(15)
    f.write(data + str(i)+',')
    f.write(f"Status Code: {resp.status_code}"+',')
    f.write(f"Response Text: {resp.text}"+'\n')
