import requests
import re, datetime
import schedule, time

url = "https://www.kma.go.kr/w/rss/dfs/hr1-forecast.do?zone=4157058000"

def get_weather_information():
  response = requests.get(url)
  wfor = re.findall("<wfKor>(.+)</wfKor>", response.text)[0]
  temp = re.findall("<temp>(.+)</temp>", response.text)[0]
  humi = re.findall("<reh>(.+)</reh>", response.text)[0]
  print("=======실시간 날씨 예보=======")
  print("기상상태: {}".format(wfor))
  print("현재온도: {}°C".format(temp))
  print("현재습도: {}%".format(humi))

schedule.every(10).seconds.do(get_weather_information)

while True:
  now = datetime.datetime.now()
  now = now.strftime("%Y/%n/%d %H:%S")
  schedule.run_pending()
  time.sleep(2)