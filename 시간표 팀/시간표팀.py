def getLunch(today):
    import requests, json

    schul_dept_code = 'J10'
    schul_code = '7531103'

    url = 'http://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN18620200826103326268120&infSeq=1&bgs=Y   ' #사이트에 기재된 API 요청 주소
    parameters = {
        'KEY' : 'bdb5882ef04444ba98ba8e621b20aea9',         #사이트에서 발급받은 API 인증키
        'Type' : 'json',                                    #받아올 데이터의 자료 구조
        'ATPT_OFCDC_SC_CODE' : schul_dept_code,         
        'SD_SCHUL_CODE' : schul_code,               #각각에 대한 설명은 API 사이트에 설명되어 있다.
        'MLSV_FROM_YMD' : today,
        'MLSV_TO_YMD' : today
    }
    response = requests.get(url, params=parameters)
    print(response.text)
    # response_json = json.loads(response.text)
    # lunch_menu = response_json['mealServiceDietInfo']['1']['DDISH_NM']

print(getLunch('230913'))