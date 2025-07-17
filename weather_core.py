# weather_core.py
import requests
import os
from dotenv import load_dotenv

def get_lat_lon(city):
    # TODO: 도시 이름을 위도/경도로 바꾸는 코드
    pass

def get_weather(lat, lon):
    # TODO: 날씨와 자외선 정보 받아오는 코드
    pass

def get_air_quality(lat, lon):
    # TODO: 미세먼지 정보 받아오는 코드
    pass

def analyze(uvi, pm25):
    # TODO: 자외선/미세먼지 수치 기반 경고 메시지 만들기
    pass

def menu():
    # TODO: 사용자에게 어떤 항목을 볼지 고르게 하기
    pass

def main():
    # TODO: 전체 흐름 조절 (도시입력 → 메뉴선택 → API 호출 → 결과출력)
    pass

if __name__ == "__main__":
    main()
