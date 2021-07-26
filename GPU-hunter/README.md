# GPU-hunter
11번가의 리더스시스템즈 RTX FE 시리즈 구매 매크로입니다.
#### Reminder
이 README는 Windows 환경에서 표준 Chrome 빌드를 사용하는 일반적인 사용자를 위해 작성했습니다.  
보다 특수한 환경에서 사용하는 경우 그에 맞춰 `main.py`를 적절히 수정해야 합니다.

## Prerequisites
GPU-hunter는 **파이썬 3**과 **구글 크롬**을 필요로 합니다. 설치되어 있지 않다면 먼저 설치합니다.

## Configuration
1. Python 종속성 모듈 설치  
`Windows + R` 키를 누르고 `cmd`를 입력한 후 다음 명령어를 입력합니다.  
```
pip install python-dotenv opencv-python numpy selenium
```

2. Chrome 빌드 버전 확인  
Chrome을 열고 *Chrome 메뉴 - 도움말 - Chrome 정보*에서 Chrome의 빌드 버전을 확인합니다.  
버전 숫자의 맨 앞 자리만 기억하면 됩니다. 현재 최신 빌드는 92입니다.

3. ChromeDriver 다운로드  
[ChromeDriver 다운로드 페이지](https://chromedriver.chromium.org/downloads)에서 자신의 Chrome 버전과 일치하는 ChromeDriver를 다운로드합니다.  
`chromedriver_win32.zip`을 다운로드하고 압축을 풀어 `chromedriver.exe`를 `main.py`와 같은 폴더 안에 둡니다.

4. `.env` 환경 변수 설정  
`sample.env`의 파일명을 `.env`로 바꾸고 파일을 열어 비어있는 값들을 다음과 같이 편집한 후 저장합니다.

|Key|Value|
|:-:|:---:|
|id|11번가 ID|
|pw|11번가 비밀번호|
|skpaypw|SK페이 간편비밀번호 6자리|
|mode|`3070` or `3080` or `test`|

mode 값이 `3070` 또는 `3080`일 경우 리더스시스템즈 해당 제품에 대해 시도합니다.  
`test`일 경우 미리 준비된 테스트 URL에 대해 시도합니다.
#### Other Options
> productURL*key* 키를 추가하고 값으로 원하는 제품의 URL을 설정한 다음, mode값을 *key*로 설정하면 해당 제품에 대해 시도합니다.

> `purchase`의 값이 1이 아니라면 마지막 간편비밀번호 입력을 콘솔에서 시뮬레이션만 하고 실제로 수행하지 않습니다. 테스트 시에 이용하세요.

> *Canary* 또는 *Dev* 등 Chrome의 표준 빌드를 사용하지 않는다면 `canary` 옵션에서 `0`을 지우고 `chrome.exe`의 경로를 입력합니다.

## Usage
1. CMD 창을 열고 `cd` 명령어를 이용해 `main.py`가 있는 폴더로 이동합니다.  
2. `python main.py`를 입력합니다.  
3. 우측의 개발자 도구 좌측 상단에 있는 Elements 좌측의 직사각형이 겹친 아이콘 `Toggle device toolbar` 버튼을 클릭하고 콘솔로 돌아와 엔터를 누릅니다.

다음은 프로그램이 자동으로 수행하는 작업입니다.
1. 로그인 절차를 수행한 다음 제품 페이지로 이동합니다.  
2. 제품이 판매중이 아니라면 판매가 시작될 때까지 새로고침을 반복합니다.  
이 과정에서 `keys`라는 이름의 작은 창이 생성됩니다. 클릭하면 *응답 없음*으로 표시될 수 있으나, 무시하고 해당 창에 포커스 상태를 유지합니다.
3. 판매가 시작되면 두번째 옵션을 선택하고 구매 버튼을 눌러 결제를 진행합니다.  
4. **중요** SK Pay 간편결제 비밀번호 입력 창으로 이동하면, `keys` 창에 다음과 같은 숫자 이미지가 표시됩니다.
```
1 2 3 4   5 6 7 8 9 0
```
<img src='skpay/ex.jpg'>
  위 예시처럼 두 숫자만 멀리 떨어져 있는 이미지가 표시됩니다. 떨어진 부분의 **왼쪽** 에 있는 숫자를 입력합니다.  
  이 경우, `keys` 창에 포커스가 된 상태로 `4`을 입력해야 합니다. 반드시 포커스 상태에서 한 번에 정확하게 입력해야 합니다.

5. 프로그램이 자동으로 결제 비밀번호를 입력하고 ARS 요청까지 완료합니다. ARS를 마친 후 직접 인증 완료 버튼을 클릭하세요.

## Demo
