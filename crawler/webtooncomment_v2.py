#-*- coding:utf-8 -*-
import time
import sys
from selenium import webdriver

from urllib.request import urlopen
from bs4 import BeautifulSoup

######
def extract_date(string) :
    return string[:10].replace("-", ".")
######

print("titleId :" , end="")
titleId = input()
print("start : ", end="")
start = int(input())
print("end : ", end="")
end = int(input())

html = urlopen("https://comic.naver.com/webtoon/detail.nhn?titleId=183559&no=383")
bs0bj = BeautifulSoup(html, "html.parser")

upload_date = bs0bj.find(class_="date").text # 웹툰 게시한 날짜
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
driver.implicitly_wait(5)
# 웹 페이지 로드 기다림(5sec)
# driver.get 시에만 적용되는듯

f = open('comments.txt', 'w')

try :
    for no in range(383, 383 + 1) : 
        driver.get("http://comic.naver.com/comment/comment.nhn?titleId=183559&no=383")

        driver.find_element_by_css_selector('.u_cbox_btn_view_comment').click() # 전체 댓글 보기 클릭
        time.sleep(0.3)
        driver.find_element_by_css_selector('.u_cbox_next_end').click()
        time.sleep(0.3)


        for i in range(0, 100) :
            count = len(driver.find_elements_by_css_selector('.u_cbox_num_page')) - 1
            print(i)
            for n in range(count, -1, -1) : # 9 ~ 0
                index = driver.find_elements_by_css_selector('.u_cbox_num_page')
                # 페이지 새로 로드할 때마다 읽어와야함
                index[n].click()
                time.sleep(0.3)
                comment_contents = driver.find_elements_by_css_selector('.u_cbox_contents')
                comment_dates = driver.find_elements_by_css_selector('.u_cbox_date')

                for d in range(0, len(comment_dates)) :
                    comment_dates[d] = extract_date(comment_dates[d].get_attribute('data-value'))
                    # 댓글 쓴 날짜, 비교 위해 포맷 변경
    
                for m in range(len(comment_contents) - 1, -1, -1) :
                    if comment_dates[m] == upload_date :
                        print("정상적으로 댓글 저장함, 프로그램 종료")
                        driver.quit()
                        f.close()
                        sys.exit()
                        # 업로드 날짜와 같은 날짜 댓글 발견되면 종료
                    try :
                        f.write(comment_contents[m].text + '\n')
                    except :
                        pass
                #
            #
            #1~10페이지 다 긁어오면
            nextPage = driver.find_elements_by_css_selector('.u_cbox_pre')
            nextPage[1].click()
            # "이전" 클릭
            time.sleep(0.3)
        #
    #
except Exception as ex :
    print("오류 발생", ex)
    print("종료하려면 엔터 키")
    input()

driver.quit()
f.close()