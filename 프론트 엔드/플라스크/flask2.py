from flask import Flask, render_template

app = Flask(__name__)

# "/meal" 경로에 대한 처리
@app.route('/meal', methods=['GET'])
def get_meal_info():
    # 실제로는 여기에서 데이터베이스에서 정보를 가져오는 등의 로직을 구현할 수 있습니다.
    return "<p>급식 정보</p>"

# 기본 경로에 대한 처리
@app.route('/')
def index():
    # HTML 파일을 반환
    return "ㅎㅇ"

if __name__ == '__main__':
    app.run(debug=True)