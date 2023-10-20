from datetime import date

def html(date_str):
    from datetime import datetime
    try:
        date = datetime.strptime(date_str, '%Y%m%d')
    except ValueError:
        return "올바른 날짜 형식이 아닙니다. 날짜는 'YYYYMMDD' 형식으로 입력해주세요."

    html_output = f"<p>입력한 날짜는: {date.strftime('%Y년 %m월 %d일')}</p>"

    return html_output

input_date = input()
html_result = html(input_date)
print(html_result)


import os
import json

from datetime import date

def html(date_str):
    from datetime import datetime
    try:
        date = datetime.strptime(date_str, '%Y%m%d')
    except ValueError:
        return "올바른 날짜 형식이 아닙니다. 날짜는 'YYYYMMDD' 형식으로 입력해주세요."

    html_output = f"<p>입력한 날짜는: {date.strftime('%Y년 %m월 %d일')}</p>"

    return html_output

input_date = input()
html_result = html(input_date)
print(html_result)
import json

# JSON 파일을 열고 읽기 모드로 로드
with open("급식2.json", "r", encoding="utf-8") as json_file:
    #SON 데이터를 파싱하여 파이썬 객체로 변환
    급식 = json.load(json_file)

# JSON 데이터에서 "EVENT_NM" 값을 추출
event_name = 급식.get("EVENT_NM")

# 추출한 값을 출력
if event_name is not None:
    print("Event Name:", event_name)
else:
    print("EVENT_NM not found in the JSON file.")
