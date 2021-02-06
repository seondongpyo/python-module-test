import requests

# GET 요청
response = requests.get('http://www.google.com')

# HTTP 응답 코드
response_status_code = response.status_code
print('status code :', response_status_code)

# 응답 결과로 얻은 HTML 코드
response_text = response.text
print('text :', response_text)

