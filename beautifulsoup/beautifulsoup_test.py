import requests
from bs4 import BeautifulSoup

# 네이버에서 'beautifulsoup'을 검색한 결과를 보여주는 URL 주소
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=beautifulsoup'

response = requests.get(url)  # GET 요청 보내기

if response.status_code == 200:  # HTTP 응답 코드가 200일 경우
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')  # HTML 코드를 soup 객체로 변환
    print(soup)

else:  # 200 이외의 응답 코드를 받은 경우
    print(response.status_code)
