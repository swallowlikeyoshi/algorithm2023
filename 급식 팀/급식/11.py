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
        URL = SchoolApi.base_url + self.sub_url # sub_url ?
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
        
    # def meal(self):
    #     data = self.get_data()
    #     try:
    #         string = "<조식>\n"+data[0]["DDISH_NM"].replace("<br/>", "\n")+"\n\n"
    #         string+= "<중식>\n"+data[1]["DDISH_NM"].replace("<br/>", "\n")+"\n\n"
    #         string += "<석식>\n" + data[2]["DDISH_NM"].replace("<br/>", "\n")
    #         characters = "1234567890./-*"
    #         for x in range(len(characters)):
    #             string = string.replace(characters[x],"")
    #         return string
    #     except:
    #         return "오늘은 급식이 없습니다."
        
    def meal(self): # SchoolAPI 안에 API를 이용해서 정보를 가져오는 메소드를 만들고, 급식 정보를 가져오는 기능은 클래스를 상속해서 따로 만들면 좋을 듯!
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
    
    SchoolApi("schoolInfo", params).get_school_info() #SchoolApi 클래스에 메소드가 없는 듯?
    msg=""

    params = {
        "MLSV_YMD": dt.now().strftime("%Y%m%d")
        }
    
    # 여기서 굳이 부가적인 설명문을 붙여야 할 필요가 없다. 왜냐하면 함수는 본인이 맡은 역할만 하면 되니까!
    # *함수가 해야할 일: 오늘 급식 메뉴를 출력한다
    # 그렇다면 함수가 해야 할 일은 단순히 급식 메뉴를 출력하는 일이지 부가적인 설명문을 붙이는 일이 아님!
    # 설명문을 붙이는 일은 이 함수를 이용하는 다른 프로그램이 해야 할 일이지, 이 함수에서 하게 되면 추후 코드 재사용이 어려워지고, 유지보수가 어려워진다.
    # 객체 지향 프로그래밍(OOP) 설계 5원칙 중 제 1원칙인 단일 책임 원칙(SRP)이 함수 설계의 중요성을 잘 알려준다. 인터넷에 검색해보면 자세한 설명을 알 수 있을 것.
    # 설계 5원칙을 잘 생각하면서 클래스와 메소드를 구성하면 좋은 코드를 짤 수 있음!

    # msg+="______오늘의 급식______\n"

    msg+=SchoolApi("mealServiceDietInfo", params).meal()

    params = { 
        "GRADE": "1",
        "CLASS_NM": "3", 
        "ALL_TI_YMD": dt.now().strftime("%Y%m%d")
        }
    msg+="\n______오늘의 시간표______\n"
    msg+=SchoolApi("hisTimetable", params).time()
    if(SchoolApi("SchoolSchedule", params).schedule()!="x"):
        msg+="______오늘의 학사일정______\n"
        msg+=SchoolApi("SchoolSchedule", params).schedule()