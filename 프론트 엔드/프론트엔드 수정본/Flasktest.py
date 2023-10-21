from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html', 
                           dietInfo = get_diet_info(),
                           weatherInfo = get_weather_info(),
                           schoolEventInfo = get_schoolEventInfo() )

def today(): #오늘 날짜를 출력하는 함수.
    return str(datetime.today().date()).replace('-', '')

def get_diet_info():
    # 여기에 백엔드 친구들이 코딩한 급식 정보를 불러오는 함수를 실행해야함.
    # 백엔드에서 코딩한 파일들을 import 해서 파일 내부의 함수를 실행하고 값을 반환하면 됨.
    return "급식 정보"

def get_weather_info():
    # 이하 동문
    return "날씨 정보"

def get_schoolEventInfo():
    # 이하 동문
    return "학사일정 정보"

if __name__ == '__main__':
    # 포트 80은 http 기본 포트임. 명시하지 않았을 경우 브라우저는 이 포트를 통해 웹사이트에 접속하려고 시도함.
    app.run(host="0.0.0.0", debug=True, port=80) 