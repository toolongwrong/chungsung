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

######
class Crawling :
    def __init__(self, Webtoon_info, Webdriver_controller, file) :
        f = open(str(file), "w", encoding="utf-8")

        try :
            for no in range( int(Webtoon_info.start), int(Webtoon_info.end) + 1 ) :
                
                upload_date = Webtoon_info.get_upload_date(no)
                Webdriver_controller.open_comments(Webtoon_info.titleId, no)

                loop = 1

                while loop != 0 :
                    print(loop) # 작동 상황 표시를 위한 출력
                    loop += 1

                    count = Webdriver_controller.get_comments_per_page()

                    for n in range(count, -1, -1) :
                        index = Webdriver_controller.get_index_list()
                        # 페이지 인덱스 읽어옴
                        index[n].click()
                        time.sleep(Webdriver_controller.sleeptime)
                        # 페이지 이동

                        comment_contents = Webdriver_controller.get_comments_content()
                        comment_date = Webdriver_controller.get_comments_date()

                        for d in range(0, len(comment_date)) :
                            comment_date[d] = extract_date(comment_date[d].get_attribute('data-value'))
                            # 댓글 문자열 가공

                        for m in range(len(comment_contents) - 1, -1, -1) :
                            if comment_date[m] != upload_date :
                                try :
                                    f.write(comment_contents[m].text + '\n')
                                except :
                                    pass
                            else : 
                                loop = 0
                                # 업로드일에 도달하면 루프 종료
                        #
                    #
                    Webdriver_controller.next_page()
                #
            #
        except Exception as ex :
            print("오류 발생", ex)
        
        print("저장 완료")
        os.system('pause')
        Webdriver_controller.driver.quit()
        f.close()
######

######
class Webtoon_info :
    def __init__(self, titleId, start, end) :
        self.titleId = titleId
        self.start = start
        self.end = end

        self.html = urlopen("https://comic.naver.com/webtoon/detail.nhn?titleId=" + str(self.titleId) + "&no=" + str(self.start))
        self.bs0bj = BeautifulSoup(self.html, "html.parser")
        self.title = self.bs0bj.find(class_="tit").text

        print("웹툰 제목 :", self.title)
        print(self.start, "부터", self.end, "까지의 댓글을 저장합니다.")

    def get_upload_date(self, no) :
        self.html = urlopen("https://comic.naver.com/webtoon/detail.nhn?titleId=" + str(self.titleId) + "&no=" + str(no))
        self.bs0bj = BeautifulSoup(self.html, "html.parser")
        self.upload_date = self.bs0bj.find(class_="date").text
        print("웹툰 업로드 : ", self.upload_date)
        
        return self.upload_date
######

######
class Webdriver_controller:
    def __init__(self, sleeptime, headless) :
        self.sleeptime = sleeptime

        if headless == 1 :
            # headless option
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            option.add_argument('window-size=1920x1080')
            option.add_argument("disable-gpu")

            self.driver = webdriver.Chrome("C:/Main/Util/chromedriver/chromedriver.exe", chrome_options=option)
        
        elif headless == 0 :
            self.driver = webdriver.Chrome("C:/Main/Util/chromedriver/chromedriver.exe")
        
        self.driver.implicitly_wait(5)

    def open_comments(self, titleId, no) :
        self.driver.get("http://comic.naver.com/comment/comment.nhn?titleId=" + str(titleId) + "&no=" + str(no))
        time.sleep(self.sleeptime)
        self.driver.find_element_by_css_selector('.u_cbox_btn_view_comment').click() # 전체 댓글 보기 클릭
        time.sleep(self.sleeptime)
        self.driver.find_element_by_css_selector('.u_cbox_next_end').click()
        time.sleep(self.sleeptime)
        # 페이지 열고 마지막 페이지까지 이동

    def next_page(self) :
        self.nextPage = self.driver.find_elements_by_css_selector('.u_cbox_pre')
        self.nextPage[1].click() # '이전' 클릭
        time.sleep(self.sleeptime)

    def get_comments_per_page(self) :
        return len(self.driver.find_elements_by_css_selector('.u_cbox_num_page')) - 1

    def get_index_list(self) :
        return self.driver.find_elements_by_css_selector('.u_cbox_num_page') 

    def get_comments_content(self) :
        return self.driver.find_elements_by_css_selector('.u_cbox_contents')

    def get_comments_date(self) :
        return self.driver.find_elements_by_css_selector('.u_cbox_date')
######

### example
# print("titleId : " , end="")
# titleId = input()
# print("start : ", end="")
# start = input()
# print("end : ", end="")
# end = input()
    
# toon = Webtoon_info(titleId, start, end)
# webd = Webdriver_controller(0.4, 0) # (sleeptime, isheadless)

# Crawling(toon, webd, 'qwe.txt')