from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from datetime import datetime
import time

logging = []

# 640 신월문화체육센터 정류장 시간표 수집
while True:
    with urllib.request.urlopen('http://bus.go.kr/busArrivePlanIfoPopup.jsp?station=114000189&busRouteId=100100093&seq=2&stationNm=%EC%8B%A0%EC%9B%94%EB%AC%B8%ED%99%94%EC%B2%B4%EC%9C%A1%EC%84%BC%ED%84%B0&wbustp=N') as response:
        # html 긁어오기
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        # 버스정류장의 버스 데이터 묶음 추출
        busstop_data = soup.find_all('li', {'class': 'info_bus'})
        #print(busstop_data)

        for bus in busstop_data:
            if not '정류소 전일 버스 운행시간' in bus.text:
                status = bus.text.strip()
                # print(status)
                # 운행종료가 아니면 곧 도착 예정이므로 캐치한다.
                # print("{}: {}".format(datetime.now().isoformat(), status))
                if status != '운행종료' and status != '출발대기':
                    tm = datetime.now().isoformat()
                    print(tm)
                    logging.append(tm)

    time.sleep(30)  # 30 seconds

print(logging)
