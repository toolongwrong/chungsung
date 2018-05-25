#-*- coding:utf-8 -*-
import time
import sys
from selenium import webdriver

titleId = str(sys.argv[1])
start = int(sys.argv[2])
end = int(sys.argv[3])

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

for no in range(start, end + 1) : 
    
    driver.get('http://comic.naver.com/comment/comment.nhn?titleId=' + titleId + '&no=' + str(no))

    driver.find_element_by_css_selector('.u_cbox_btn_view_comment').click()
    time.sleep(0.5) # 페이지 로드되는 시간
    # 전체 댓글 보기 클릭

    for i in range(0, 5) :
        for n in range(0, 10) :
            index = driver.find_elements_by_css_selector('.u_cbox_num_page')
            # 페이지 새로 로드할 때마다 읽어와야함
            index[n].click()
            time.sleep(0.1)
            comments = driver.find_elements_by_css_selector('.u_cbox_contents')
            for m in comments :
                try :
                    f.write(m.text + '\n')
                except :
                    pass
        #1~10페이지 다 긁어오면
        nextPage = driver.find_element_by_css_selector('.u_cbox_next')
        nextPage.click() # "다음" 클릭
        time.sleep(0.1)
#

driver.quit()
f.close()

print("done.")