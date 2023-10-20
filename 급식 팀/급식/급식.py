import requests, json
import time

schul_dept_code = 'J10'
schul_code = '7531103'
today = time.strftime('%Y%m%d')

url = 'https://open.neis.go.kr/hub/mealServiceDietInfo' #사이트에 기재된 API 요청 주소
parameters = {
    'KEY' : 'b72c971c69c14bfe87cecb165d696fbf',         #사이트에서 발급받은 API 인증키
    'Type' : 'json',                                    #받아올 데이터의 자료 구조
    'ATPT_OFCDC_SC_CODE' : schul_dept_code,         
    'SD_SCHUL_CODE' : schul_code,               #각각에 대한 설명은 API 사이트에 설명되어 있다.
    'MLSV_FROM_YMD' : today,
    'MLSV_TO_YMD' : today
}
response = requests.get(url, params=parameters)
jsonfile = json.loads(response.text)


print(jsonfile['mealServiceDietInfo','row','DDISH_NM'])



