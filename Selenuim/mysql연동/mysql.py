import pymysql
from selenium import webdriver
import time

#DB
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='likelion',
    charset='utf8'
)

cursor = conn.cursor();

#Chrome Headless option
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

#크롬 드라이버로 크롤러 객체 설정
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.get('https://comic.naver.com/webtoon/list.nhn?titleId=318995&weekday=fri')
time.sleep(0.5)

titles=driver.find_elements_by_css_selector('td.title a')

for title in titles:
    print(title.text)
    SQL = "insert into `test`(`title`,`url`) values ('%s', '%s')" %(title.text, title.get_attribute('href'))
    cursor.execute(SQL)

conn.commit()