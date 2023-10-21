


def html(date_str):
    from datetime import datetime
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return "올바른 날짜 형식이 아닙니다. 날짜는 'YYYY-MM-DD' 형식으로 입력해주세요."

    html_output = f"<p>입력한 날짜는: {date.strftime('%Y년 %m월 %d일')}</p>"

    return html_output

    input_date = input()
    html_result = html(input_date)
    print(html_result)



import requests

schul_dept_code = 'J10'
schul_code = '7531103'
today = '20230911'

url = 'https://open.neis.go.kr/hub/SchoolSchedule' #사이트에 기재된 API 요청 주소
parameters = {
    'KEY' : 'e996f241412f459db296a417a481a358',         #사이트에서 발급받은 API 인증키
    'Type' : 'json',                                    #받아올 데이터의 자료 구조
    'ATPT_OFCDC_SC_CODE' : schul_dept_code,         
    'SD_SCHUL_CODE' : schul_code,               #각각에 대한 설명은 API 사이트에 설명되어 있다.
    'MLSV_FROM_YMD' : today,
    'MLSV_TO_YMD' : today
}   
response = requests.get(url, params=parameters)
print(response.text)