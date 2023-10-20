


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
{
    "mealServiceDietInfo": [
        {
            "head": [
                {
                    "list_total_count": 1
                },
                {
                    "RESULT": {
                        "CODE": "INFO-000",
                        "MESSAGE": "정상 처리되었습니다."
                    }
                }
            ]
        },
        {
            "row": [
                {
                    "ATPT_OFCDC_SC_CODE": "J10",
                    "ATPT_OFCDC_SC_NM": "경기도교육청",
                    "SD_SCHUL_CODE": "7531103",
                    "SCHUL_NM": "운양고등학교",
                    "MMEAL_SC_CODE": "2",
                    "MMEAL_SC_NM": "중식",
                    "MLSV_YMD": "20230911",
                    "MLSV_FGR": 1000.00,
                    "DDISH_NM": "칼슘기장밥 <br/>얼갈이배추된장국 <br/>닭갈비 <br/>연근부각 <br/>총각김치 <br/>생크림요거트(개별) ",
                    "ORPLC_INFO": "쇠고기(종류) : <br/>쇠고기 식육가공품 : <br/>돼지고기 : <br/>돼지고기 식육가공품 : <br/>닭고기 : 국내산<br/>닭고기 식육가공품 : <br/>오리고기 : <br/>오리고기 가공품 : <br/>쌀 : 국내산<br/>배추 : 국내산<br/>고춧가루 : 국내산<br/>콩 : 국내산<br/>낙지 : <br/>고등어 : <br/>갈치 : <br/>오징어 : <br/>꽃게 : <br/>참조기 : <br/>비고 : ",
                    "CAL_INFO": "778.1 Kcal",
                    "NTR_INFO": "탄수화물(g) : 115.5<br/>단백질(g) : 41.1<br/>지방(g) : 15.7<br/>비타민A(R.E) : 221.0<br/>티아민(mg) : 0.6<br/>리보플라빈(mg) : 0.6<br/>비타민C(mg) : 32.7<br/>칼슘(mg) : 1373.2<br/>철분(mg) : 3.2",
                    "MLSV_FROM_YMD": "20230911",
                    "MLSV_TO_YMD": "20230911"
                }
            ]
        }
    ]
}