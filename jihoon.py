'''
from selenium import webdriver
#driver1=webdriver.Chrome()


w=1920/2
h=1080/2

d=[]
pos=[(0,0),(w,0),(0,h),(w,h)]
for i in range(4):
    driver=webdriver.Chrome()
    driver.get("http://www.youtube.com")
    d.append(driver)
    driver.set_window_size(w,h)
    driver.set_window_position(pos[i][0],pos[i][1])

from selenium import webdriver#여기서부터
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
driver.get("http://www.youtube.com")#여기까지 커맨드 없어지게 만드는 프로그램
    
    
    
#driver.set_window_size(200,300)
#import time
#u=["100","200","300","400","111117"]
#for i in range(len(u)):
    #driver.set_window_position(i*100,i*100)
    #time.sleep(1)
 


'''
#창 사이즈 조정
'''
importt time
u=["100","200","300","400"]

or i in range(len(u)):
for i in range(len(u))
driver.maximize_window()    
    
    
    
driver1.get("http://www.google.com")



driver.maximize_window()#창 최대화
driver.minimize_window()#창 최소화
driver.set_window_size(200,300)#창 사이즈 조정
driver.set_window_position(0,0)#창 위치 설정


u=["http://youtube.com","http://naver.com","http://google.com"]
d=[]
import time
for i in range(len(u)):
    driver=webdriver.Chrome()
    d.append(driver)
    time.sleep(1)

for i in range(len(u)):
    d[i].get(u[i])

input("엔터를 치면 창이 닫힙니다.종료할까요?")
d[i].close()
'''



#테스트 싸이트 웹크롤링#피자 아저씨 홈페이지
'''
from selenium import webdriver#여기서부터
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/")#여기까지 커맨드 없어지게 만드는 프로그램
p='//*[@id="homePageLinks"]/ul/li'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_firstName"]'
e=driver.find_element('xpath',p)
e.send_keys("backgoori")

p='//*[@id="id_lastName"]'
e=driver.find_element('xpath',p)
e.send_keys("jic")

p='//*[@id="id_gender_0"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_username"]'
e=driver.find_element('xpath',p)
e.send_keys("niddongcaladdong")

p='//*[@id="id_password"]'
e=driver.find_element('xpath',p)
e.send_keys("55555")

p='//*[@id="id_state"]/option[2]'
e=driver.find_element('xpath',p)
e.click()


p='//*[@id="id_fee"]/option[4]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_date"]'
e=driver.find_element('xpath',p)
e.send_keys("11/17/2023")

p='/html/body/form/div/input'
e=driver.find_element('xpath',p)
e.click()
'''
#엔터 치기
'''
from selenium.webdriver.common.keys import keys
e.send_keys(Keys.RETURN)


'''
#웹툰 들어가기

import time
from selenium import webdriver#여기서부터
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

q=["전지적 독자시점"]
driver.get("https://comic.naver.com/search?keyword="+q[0])
time.sleep(2)

time.sleep(3)
p='//*[@id="content"]/div[2]/ul/li[1]/div/a/span/span'
e=driver.find_element('xpath',p)
e.click()



#유튜브에서 검색(마프리에요...)
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
driver.get("https://www.youtube.com/results?search_query=마플")

p1='//a[@id="thumbnail"]'
elements=driver.find_elements('xpath',p1)

time.sleep(3)

print(elements[1].get_attribute("href"))
driver.get(elements[1].get_attribute("href"))
'''
#필요 없음
'''
time.sleep(2)
p='//input[@id="search"]'
e=driver.find_element('xpath',p)
#e.send_keys(마플)

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)
time.sleep(3)

'''


#텍스트 파일로 저장하기
'''
text="눈누난나"
file=open('텍스트.txt','w')
file.write(text)
file.close()

'''
#학교종이(늘봄초)
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://v4.schoolbell-e.com/ko/gate/login")
time.sleep(3)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[1]/div[1]/phone-number-input/div/input'
e=driver.find_element('xpath',p)
e.send_keys("01092504131")
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[2]/div/input'
e=driver.find_element('xpath',p)
e.send_keys("8080")
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[3]/button'
e=driver.find_element('xpath',p)
e.click()

time.sleep(2)
p='/html/body/app-root/app-main/div[1]/app-main-home/div[2]/div[1]/div[1]/app-my-group-slides/div/ngu-carousel/div/div[1]/div/ngu-tile[1]/div/div[1]/div/div[1]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(2)


file=open('학교종이.txt','w')
for i in range(10):
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div[3]/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element('xpath',p)
    file.write(e.text+'\n')
file.close()
'''
#<네이버 뉴스 검색창 스크린캡처 하기>

'''
k=["이수인","송현진","고가윤",]
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
time.sleep(2)


for i in range(len(k)): 
    driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+k[i])
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    driver.save_screenshot(k[i]+".png")




'''








