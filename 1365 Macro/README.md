# 1365 봉사활동신청 자동화 프로그램
Selenium-based Automation Tool

## 0. 주의사항
1. 크롬 웹 드라이버를 사용하는 프로그램입니다. 정상적인 경로로 설치된 구글 크롬 브라우저가 로컬에 존재해야 동작합니다.
2. 테스트 모드 `tester.bat` 은 임의의 무작위 봉사활동에 신청 확인 직전까지 진행하는 동작 테스트 도구입니다.  
실제 신청 시 `control.bat` 을 사용하세요.


## 1. 다운로드

1. `Controller.zip` [다운로드](https://github.com/luftaquila/Web-Automation/releases/)
    * 최신 릴리즈 버전은 `v1.2.0`입니다.
2. *Controller.zip은(는) 위험할 수 있으므로 다운로드하지 않습니다.* 경고 출력 시 옆의 `^` 아이콘 클릭
3. `계속(k)` 클릭
4. `Controller.zip` 압축 해제

## 2. 사용 방법

* 테스트 모드 실행 시 `tester.bat` 실행
* 실제 신청 시도 시 `control.bat` 실행

1. *Windows의 PC 보호* 알림창 팝업 시 __추가 정보__ 클릭
2. `실행` 클릭
3. 봉사활동을 신청할 1365 계정의 아이디 및 비밀번호 입력
4. 요일 입력 : 토요일 신청 시 1, 일요일 신청 시 2 입력
5. *Windows 보안 경고* 방화벽 팝업 시 `액세스 허용(A)` 클릭  

6. 이후 모든 동작은 프로그램이 자동으로 수행합니다.

## 3. Troubleshooting
    
### 1. *ERROR_NTP_Server_not_responding*
표준시간 동기화를 위한 NTP 타임 서버가 응답하지 않는 경우.  
한국 표준 NTP 타임 서버 풀 *kr.pool.ntp.org*이 응답하지 않는 경우, 구글 NTP 타임 서버 *time.google.com*에 동기화 시도.  
두 서버가 모두 응답하지 않을 경우 컴퓨터의 로컬 시간을 사용. 시간이 맞지 않을 수 있습니다.  

### 2. *ERROR_chrome_not_installed*
브라우저 실행 단계에서 정상적인 크롬 설치를 발견할 수 없는 경우.  
[크롬 재설치](https://www.google.com/intl/ko_ALL/chrome/) 권장
     
### 3. *ERROR_login_failure_not_visible*
반응형 웹의 HTML 구조 변화로 로그인 버튼을 찾을 수 없는 경우.  
프로그램이 자동으로 로그인 재시도.

### 4. *ERROR_login_failure_wrong_info*
로그인 시도가 실패한 경우.  
프로그램이 처음부터 다시 실행. ID 및 PW 재입력.

### 5. *ERROR_stale_element_reference_exception*
타겟 요소를 선택할 수 없는 경우.  
프로그램이 자동으로 최대 5회, 0.2초 간격으로 재선택 시도.  

### 6. *ERROR_no_result*
선택할 수 있는 봉사활동 검색 결과가 존재하지 않는 경우.  
프로그램이 자동으로 최대 5회, 0.2초 간격으로 재선택 시도.  

### 7. *ERROR_maximum_attempt_count_exceeded*
프로그램이 타겟 요소 선택을 5회 재시도했음에도 선택할 수 없는 경우.  

### 8. *ERROR_not_appliable*
봉사활동 상세 페이지에 신청하기 버튼이 존재하지 않는 경우.

### 7. *ERROR_no_available_date*
봉사활동에 모집중 상태인 날짜가 존재하지 않는 경우.  
다음 달에 가능한 날짜가 존재하는지 체크 시도.

### 8. *ERROR_not_available_next_month*
다음 달에 신청 가능한 봉사활동이 존재하지 않는 경우.  
