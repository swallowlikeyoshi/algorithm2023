import requests
import json

class SchoolApi:

    params = {
        "KEY": "b72c971c69c14bfe87cecb165d696fbf",
        "Type": "json",
    }

    schoolinfo = {}

    base_url = "https://open.neis.go.kr/hub/"

    def get_data(self):
        URL = SchoolApi.base_url + self.sub_url
        self.params.update(SchoolApi.params)
        self.params.update(SchoolApi.schoolinfo)
        response = requests.get(URL, params=self.params)

        try:
            j_response = json.loads(response.text)[self.sub_url]
            if j_response[0]["head"][0]["list_total_count"] == 1:
                return j_response[1]["row"][0]
            else:
                return j_response[1]["row"]
        except:
            print("찾는 데이터가 없습니다.")
            return response.text
        
    def meal(self):
        data = self.get_data()
        try:
            string = "<조식>\n"+data[0]["DDISH_NM"].replace("<br/>", "\n")+"\n\n"
            string+= "<중식>\n"+data[1]["DDISH_NM"].replace("<br/>", "\n")+"\n\n"
            string += "<석식>\n" + data[2]["DDISH_NM"].replace("<br/>", "\n")
            characters = "1234567890./-*"
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            return string
        except:
            return "오늘은 급식이 없습니다."
        
    def meal(self):
        data = self.get_data()
        try:
            string = "<조식>\n"+data[0]["DDISH_NM"].replace("<br/>", "\n")+"\n\n"
            string+= "<중식>\n"+data[1]["DDISH_NM"].replace("<br/>", "\n")+"\n\n"
            string += "<석식>\n" + data[2]["DDISH_NM"].replace("<br/>", "\n")
            characters = "1234567890./-*"
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            return string
        except:
            return "오늘은 급식이 없습니다."

from datetime import datetime as dt

if __name__ == "__main__":
    params = {
        "SCHUL_NM": "운양고등학교"
    }
    SchoolApi("schoolInfo", params).get_school_info()
    msg=""

    params = {"MLSV_YMD": dt.now().strftime("%Y%m%d")}
    msg+="______오늘의 급식______\n"
    msg+=SchoolApi("mealServiceDietInfo", params).meal()

    params = {"GRADE": "1", "CLASS_NM": "3", "ALL_TI_YMD": dt.now().strftime("%Y%m%d")}
    msg+="\n______오늘의 시간표______\n"
    msg+=SchoolApi("hisTimetable", params).time()
    if(SchoolApi("SchoolSchedule", params).schedule()!="x"):
        msg+="______오늘의 학사일정______\n"
        msg+=SchoolApi("SchoolSchedule", params).schedule()