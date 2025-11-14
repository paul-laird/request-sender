import sys
import requests
import time
import argparse
import json

url = sys.argv[2]
data = sys.argv[3]
num= int(sys.argv[4])
interval=int(sys.argv[5])
fn=sys.argv[1]
parser = argparse.ArgumentParser(description='A simple script demonstrating argparse with defaults.')
parser.add_argument('--var', type=str, default='page', help='The element of json data that will increment.')
args = parser.parse_args()
var=args.var

def sendRequests(fn,url,data,num,interval,var):
  with open(fn,'w') as f:
    for i in range(num):
      j=json.loads(data)
      j[var]=i
      data=json.dumps(j)
      resp = requests.post(url, data=data)
      time.sleep(15)
      f.write(data + str(i)+',')
      f.write(f"Status Code: {resp.status_code}"+',')
      f.write(f"Response Text: {resp.text}"+'\n')
      if not i%10:
        f.flush()
