def html(date_str):
    from datetime import datetime
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return "올바른 날짜 형식이 아닙니다. 날짜는 'YYYY-MM-DD' 형식으로 입력해주세요."

    html_output = f"<p>입력한 날짜는: {date.strftime('%Y년 %m월 %d일')}</p>"

    return html_output