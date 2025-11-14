import sys
import requests
import time
url = 'https://helloworld.requestcatcher.com/'+sys.argv[2]
data = f'{sys.argv[3]}! '

with open(sys.argv[1],'w') as f:
  for i in range(10000):
    resp = requests.post(url, data=data + str(i))
    time.sleep(15)
    f.write(data + str(i)+',')
    f.write(f"Status Code: {resp.status_code}"+',')
    f.write(f"Response Text: {resp.text}"+'\n')
    if not i%10:
      f.flush()
