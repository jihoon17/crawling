from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags = CREATE_NO_WINDOW   
driver = webdriver.Chrome(service = serv)


import time, datetime, os#시간,날짜,파일
import openpyxl

now= str(datetime.datetime.now())[:16]#지금 시간을 문자로 저장.15번째 칸까지 자르기
folderName=now.replace(':','_')#시간의 :을 _로 바꿈

os.mkdir(folderName)#폴더 만들기(변수 이름(폴더 이름))
key_word=["테슬라","세종시","청소년 도박","중학생 마약"]
wb= openpyxl.Workbook()

for i in range(len(key_word)): # key_word의 길이 반복
    ws=wb.create_sheet()   #워크시트
    ws.title=key_word[i]
    url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + key_word[i]
    driver.get(url)
    time.sleep(2)
