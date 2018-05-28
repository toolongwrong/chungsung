#-*- coding:utf-8 -*-
import time
import sys
import os
from selenium import webdriver

from urllib.request import urlopen
from bs4 import BeautifulSoup

######
def extract_date(string) :
    return string[:10].replace("-", ".")
######

sleeptime = 0.5

print("titleId :" , end="")
titleId = input()
print("start : ", end="")
start = input()
print("end : ", end="")
end = input()

html = urlopen("https://comic.naver.com/webtoon/detail.nhn?titleId=" + titleId + "&no=" + str(start))
bs0bj = BeautifulSoup(html, "html.parser")

title = bs0bj.find(class_="tit").text # 웹툰 제목

print("웹툰 제목 :", title)
print(start, "부터", end, "까지의 댓글을 저장합니다.")

# headless option
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('window-size=1920x1080')
option.add_argument("disable-gpu")
#

driver = webdriver.Chrome("C:/Main/Util/chromedriver/chromedriver.exe", chrome_options=option)
# driver = webdriver.Chrome("C:/Main/Util/chromedriver/chromedriver.exe")
driver.implicitly_wait(5)
# 웹 페이지 로드 기다림(5sec)
# driver.get 시에만 적용되는듯

f = open('comments', 'w', encoding='utf-8')

try :
    for no in range( int(start), int(end) + 1) : 

        html = urlopen("https://comic.naver.com/webtoon/detail.nhn?titleId=" + titleId + "&no=" + str(no))
        bs0bj = BeautifulSoup(html, "html.parser")
        upload_date = bs0bj.find(class_="date").text # 웹툰 게시한 날짜
        print("웹툰 업로드 : ", upload_date)

        driver.get("http://comic.naver.com/comment/comment.nhn?titleId=" + titleId + "&no=" + str(no))

        driver.find_element_by_css_selector('.u_cbox_btn_view_comment').click() # 전체 댓글 보기 클릭
        time.sleep(sleeptime)
        driver.find_element_by_css_selector('.u_cbox_next_end').click()
        time.sleep(sleeptime)

        loop_flag = 1

        while loop_flag != 0 :
            print(loop_flag) # 작동 중임을 표시하려고 출력함
            loop_flag += 1

            count = len(driver.find_elements_by_css_selector('.u_cbox_num_page')) - 1

            for n in range(count, -1, -1) : # 9 ~ 0
                index = driver.find_elements_by_css_selector('.u_cbox_num_page')
                # 페이지 새로 로드할 때마다 읽어와야함
                index[n].click()
                time.sleep(sleeptime)
                comment_contents = driver.find_elements_by_css_selector('.u_cbox_contents')
                comment_dates = driver.find_elements_by_css_selector('.u_cbox_date')

                for d in range(0, len(comment_dates)) :
                    comment_dates[d] = extract_date(comment_dates[d].get_attribute('data-value'))
                    # 댓글 쓴 날짜, 비교 위해 포맷 변경
    
                for m in range(len(comment_contents) - 1, -1, -1) :
                    if comment_dates[m] != upload_date :
                        try :
                            temp = comment_contents[m].text + '\n'
                            temp.encode('utf-8')
                            f.write(temp)
                        except :
                            pass
                    else :
                        loop_flag = 0
                #
            #1~10페이지 다 긁어오면
            nextPage = driver.find_elements_by_css_selector('.u_cbox_pre')
            nextPage[1].click() # '이전' 클릭
            time.sleep(sleeptime)
        #
    #
except Exception as ex :
    print("오류 발생", ex)

print("저장 완료")
os.system('pause')
driver.quit()
f.close()