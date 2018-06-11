py_shell.js
-> 파이썬 로직 수행하고 결과값 클라이언트 서버에 보내는 서버 파일

/tensorflow/t.py
-> 데이터를 학습하고 예측값을 도출해 낼 텐서플로우 코드
디비 연결이 되지 않아 하드코딩한 데이터로 학습함
최종 출력되는 Y 값이 예측한 결과값이며
1이 긍정적인 댓글이 현재 화 보다 다음 화에 많을 것으로 예측하는 것이고
0은 다음 화에는 더 적어질 것으로 예측한 것이다

index.html
-> 클라이언트 서버
콘솔에서 해당 폴더로 이동한 다음
live-server --port=5500
으로 실행하면 클라이언트 서버가 열린다. 5500포트만 열어뒀음
알아서 index.html 파일이 열림

* 실행하려면
npm install express
npm install python-shell
npm install live-server -g