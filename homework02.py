# http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201 : KRX 정보데이터시스템 전종목 기본정보
# https://finance.naver.com/item/sise_day.nhn?code={}&page={} : naver 일별시세 주소
import requests
import pandas as pd


url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"  # api 요청주소
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
data = {"bld": "dbms/MDC/STAT/standard/MDCSTAT01901",
"mktId": "ALL",
"share": "1",
"csvxls_isNo": "false"}  # post로 보낼 값
r = requests.post(url, headers=head, data=data)  # 리턴받음
# a = [x['ISU_SRT_CD'] for x in r.json()['OutBlock_1']]
# print(a)

# import pickle
# print(locals())  # locals를 쓰면 한 번이라도 썼던 죽지 않은 변수들이 남아있다. 딕트 형태 키 값으로 불러옴
# locals()['Butter'] = "BTS"  # 동적 변수 만들기?
# mydata = {
#     "url" : url,
#     "header" : head,
#     "data" : data,
#     "result" : r.json()['OutBlock_1']
# }
#
# with open("./mydata.pkl", "wb") as f:
#     pickle.dump(mydata, f)

Ticker = []
for i in r.json()['OutBlock_1']:
    # print(i)
    Ticker.append([i['ISU_SRT_CD'], i['ISU_NM']])
#
for j in Ticker:
    print(j[1])
    for k in range(1,4):
        url = f"https://finance.naver.com/item/sise_day.nhn?code={j[0]}&page={k}"
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        r = requests.get(url, headers=head)
        print(pd.read_html(r.text)[0].dropna())
        print()
    print("\n===========================================================\n\n")

#  딕셔너리를 pandas 사용하면 엑셀로 만들수 있다.
# print(pd.DataFrame(r.json()['OutBlock_1']))