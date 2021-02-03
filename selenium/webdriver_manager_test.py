from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 현재 클라이언트에 설치된 Chrome 버전에 해당하는 chromedriver를 찾아서 다운로드
installed_chrome_driver = ChromeDriverManager().install()
driver = webdriver.Chrome(installed_chrome_driver)
driver.get('http://www.google.com')
