# Navercafe_Auto_Comment v1

## 개요

네이버카페 댓글을 자동으로 달아주는 매크로 프로그램입니다.
공지에 있는 글을 상위부터 순차적으로 접근하고 댓글을 안달았던 글만 자동으로 댓글을 달아줍니다.  
중복 여부는 좋아요로 체크합니다.

## 기능

실행하면 아이디 비밀번호를 입력받은 뒤,  
정해진 카페로 가서 공지사항 첫 글부터 확인합니다.
중복을 체크해 댓글을 모두 작성하고 나면 브라우저를 종료합니다.

- 네이버카페 공지에 댓글을 작성하는 것으로 제작되었습니다.(다른 용도를 원하시면 코드를 수정해주세요.)
- 크롬으로 작동합니다.

## 메커니즘

1. 네이버 로그인 페이지 접속
2. 아이디 로그인
3. 지정된 카페로 이동
4. 공지사항 상위 글부터 확인
5. 좋아요 클릭 여부 확인하여 중복 확인.
6. 중복이 아닐 때 좋아요 클릭.
7. 새 댓글 2개 작성(내용 임의)
8. 다음 공지글로 이동
9. 중복이 나올 때까지 5~8번 반복
10. 중복이 나오면 브라우저 종료

## 사용법

코드 상 아이디, 비밀번호를 입력하고 원하는 카페 주소를 넣습니다.
그러면 최대 10회까지 첫번째 공지부터 확인하고 넘어갑니다.
횟수나 중복체크 여부 등을 수정해서 사용하셔도 무방합니다.

## 사용된 라이브러리

selenium  
pyperclip  
time

## 이후 구현 희망

- 서버에 올려놓고 실행
- 텔레그램으로 로그 받기
- 텔레그램으로 실행 조작
- 서버에서 공지 새글 지정된 시간마다 감시
- 새글 감지되면 프로그램 실행
- 아이디, 비밀번호 받는 창 구현
- 여러 아이디 추가, 삭제 기능
- 아이디 저장 옵션
- 스티커 랜덤 선택