test.js
-> 파이썬 로직 수행하고 결과값 클라이언트 서버에 보내는 서버 파일

sample.py
-> 자바스크립트에서 실행시키고, 결과물을 뱉어낼 파이썬 파일
파이썬에서 print() 해서 문자열이든 뭐든 출력하면, test.js 에서 "results" 변수에 배열로 저장된다

index.html
-> 클라이언트 서버
콘솔에서 해당 폴더로 이동한 다음
live-server --port=5500
으로 실행하면 클라이언트 서버가 열린다. 5500포트만 열어뒀음
알아서 index.html 파일 기준으로 열림

* 실행하려면
npm install express
npm install python-shell
npm install live-server -g