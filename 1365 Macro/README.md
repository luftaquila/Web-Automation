# 1365 봉사활동신청 자동화 프로그램
Selenium-based Automation Tool

## 0. 주의사항
1. 크롬 웹 드라이버를 사용하는 프로그램입니다. 정상적인 경로로 설치된 구글 크롬 브라우저가 있어야 동작합니다.
2. 테스트 모드 `tester.bat` 은 임의의 무작위 봉사활동에 신청 확인 직전까지 진행하는 동작 테스트 도구입니다.  
실제 신청 시 `control.bat` 을 사용하세요.


## 1. 다운로드

1. `Control.zip` [다운로드](https://github.com/luftaquila/Web-Automation/releases/)
2. *Control.zip은(는) 위험할 수 있으므로 다운로드하지 않습니다.* 경고 출력 시 옆의 `^` 아이콘 클릭
3. `계속(k)` 클릭
4. `Control.zip` 압축 해제

## 2. 사용 방법

* 테스트 모드 실행 시 `tester.bat` 실행
* 실제 신청 시도 시 `control.bat` 실행

1. *Windows의 PC 보호* 알림창 팝업 시 __추가 정보__ 클릭
2. `실행` 클릭
3. 봉사활동을 신청할 1365 계정의 아이디 및 비밀번호 입력
4. 요일 입력 : 토요일 신청 시 1, 일요일 신청 시 2 입력
5. *Windows 보안 경고* 방화벽 팝업 시 `액세스 허용(A)` 클릭  

6. 이후 모든 동작 자동으로 수행

## 3. Troubleshooting
### 1. *ERROR_chrome_not_installed*
브라우저 실행 단계에서 정상적인 크롬 설치를 발견할 수 없는 경우.  
[크롬 재설치](https://www.google.com/intl/ko_ALL/chrome/) 권장
     
### 2. *ERROR_login_failure_not_visible*
반응형 웹으로 인한 HTML 구조 변화로 로그인 버튼을 찾을 수 없는 경우.  
프로그램이 자동으로 로그인 재시도.

### 3. *ERROR_login_failure_wrong_info*
로그인 시도가 실패한 경우.  
프로그램이 처음부터 다시 실행됨.
    
### 4. *ERROR_NTP_Server_not_responding*
표준시간 동기화를 위한 한국 표준 NTP 타임 서버 풀이 응답하지 않는 경우.  
프로그램이 자동으로 구글 NTP 타임 서버와 동기화 재시도.

### 5. *ERROR_no_result*
봉사활동 검색 결과가 존재하지 않는 경우.  
    
### 6. *ERROR_not_appliable*
봉사활동 상세 페이지에 신청하기 버튼이 존재하지 않는 경우.

### 7. *ERROR_no_available_date*
봉사활동에 모집중 상태인 날짜가 존재하지 않는 경우.
