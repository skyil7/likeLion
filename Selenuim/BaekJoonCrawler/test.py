from selenium import webdriver
import time

#크롬 드라이버로 크롤러 객체 설정
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.acmicpc.net/login?next=%2F')
time.sleep(0.5)

password = input("password : ")

#Login
driver.find_element_by_name('login_user_id').send_keys('skyil7')
time.sleep(0.5)
driver.find_element_by_name('login_password').send_keys(password)
time.sleep(0.5)
driver.find_element_by_class_name('btn-u').click()
time.sleep(1)

#Goto Dynamic programming Problem List
driver.get('https://www.acmicpc.net/problem/tag/%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D')

#Get how much pages are exist
page = driver.find_elements_by_css_selector('ul.pagination li')
page_num = len(page)
pageLinks = driver.find_elements_by_css_selector('ul.pagination li a')
links = []

for link in pageLinks:
    links.append(link.get_attribute('href'))

problem_titles = []
problem_links = []
for i in range(0, page_num):
    if i != page_num-1:
        driver.get(links[i])
    #get Problems in current page
    problems=driver.find_elements_by_css_selector('table#problemset tbody tr td a')
    a = 0
    for problem in problems:
        if a % 3 == 0:
            problem_titles.append(problem.text)
            problem_links.append(problem.get_attribute('href'))
        a += 1


for i in range(len(problem_links)):
    print(problem_titles[i],problem_links[i])