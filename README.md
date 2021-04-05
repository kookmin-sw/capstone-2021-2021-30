# WhatSub?

~~~
WhatSub? : What's up?(인삿말) + Subtitles(자막)
  기존에 존재하는 일반 자막이 아닌, 새로운 형태의 자막, 즉 수어 자막을 의미
~~~

## 팀페이지 주소

<https://kookmin-sw.github.io/capstone-2021-30/>

## 프로젝트 소개

<img src="./img/signlang.png" width="200" height="200">

https://docs.google.com/presentation/d/1RFCkMSYYocAjv-2YBMx7p4LZh5xJnpjURCI2nXuHS_Y/edit?usp=sharing

**"수많은 영상들이 쏟아지는 오늘날, 농인들의 도움이 되고자 하는 프로젝트"**

### 개요
- 한국수화는 '한국어'가 아닙니다. 따라서 한국어는 말을 하거나 듣지 못하는 농인들에게 마치 외국어와 같다고 합니다. 즉, 농인들은 영상에 있는 일반 자막보다 수어 통역사분의 수어 자막이 더 편한 것입니다.
- 그렇기에 본 프로젝트는 수어 번역이 필요한 영상들에 대해 여러가지 작업을 거쳐 수어 번역을 한 뒤, 최종적으로 아바타 모델링을 통해 수어 자막을 보여주는 서비스를 제공하고자 합니다.

### 과정
1. 음성 데이터 추출
   - 음성 데이터를 Spectogram으로 표현
   - 수어 단어와 연결
3. 수어 데이터 추출 및 연결
   - 수어 단어의 키 포인트 좌표값 추출
   - 키 포인트 좌표값 가공
3. 그래픽 모델링
   - 가공된 키 포인트 값을 그래픽으로 표현

### 기능
- 사용자가 업로드한 영상을 번역하여 수어 자막으로 변환
- 편의성을 위해 영상 바로 옆에서 수어 자막을 재생

## 팀 소개
~~~
Name: 박상욱
Student ID: 20153177
E-Mail: apach6@naver.com
Role: 팀장, 음성 데이터 관리
~~~
~~~
Name: 김명호
Student ID: 20151772
E-Mail: kmaengggong@kookmin.ac.kr
Role: 수어 데이터 관리
~~~
~~~
Name: 박인혜
Student ID: 20165151
E-Mail: alsldjwm2@kookmin.ac.kr
Role: 아바타 모델링
~~~
~~~
Name: 조가성
Student ID: 20171704
E-Mail: 1138709428@qq.com
Role: 아바타 모델링
~~~
~~~
Name: 김유진
Student ID: 20185283
E-Mail: yujingim@kookmin.ac.kr
Role: 음성 데이터 관리
~~~
