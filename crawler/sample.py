import chungsung_crawler

print("titleId : " , end="")
titleId = input()
print("start : ", end="")
start = input()
print("end : ", end="")
end = input()
    
toon = chungsung_crawler.Webtoon_info(titleId, start, end)
# 네이버 웹툰 url에서 확인 가능한 titleId, 댓글을 가져올 회차 번호의 시작과 끝 입력
webd = chungsung_crawler.Webdriver_controller(0.4, 0)
# parameter -> (sleeptime, isheadless)
# sleeptime은 웹 페이지 이동 간의 딜레이때문에 넣은 것, 페이지 이동이 느리면 sleeptime을 늘려야 함
# isheadless는 webdriver 창을 띄워 보이게 할 지(0), 아니면 백그라운드로 실행할 지(1) 정하는 옵션

chungsung_crawler.Crawling(toon, webd, 'qwe.txt')
# 마지막 파라미터에 저장할 텍스트파일의 이름 지정