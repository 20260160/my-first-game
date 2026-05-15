# Week 11 실습



## 오늘 한 것

- PyInstaller 설치 및 빌드

1. Thonny :도구 → pip 패키지 관리 → pyinstaller 검색 → 설치

2. Thonny :도구 → 오픈 시스템 쉘  →explore.exe . → pyinstaller main.py

결과 : main.py랑 이미지,사운드 파일이 같은 폴더에 없어 실행X

- resource\_path() 함수 추가

- --add-data 옵션으로 에셋 포함

- MyGame.exe 실행 확인 → 실행O(바탕화면 복사본 실행O)



## resource_path() 를 써야 하는 이유

게임 코드에서 이미지와 사운드 파일을 불러오는 모든 부분을 resource\_path()를 사용하는 방식으로 수정하여, Python 파일 상태와 EXE 파일 상태에서 달라지는 파일 경로를 자동으로 인식하고 리소스 파일이 정상적으로 출력되도록 하기위해 사용





## 빌드 명령어

* explore.exe

* pyinstaller main.py



* 기본

pyinstaller --onefile main.py



* 터미널 창 숨기기 (배포용)

pyinstaller --onefile --windowed main.py



* 에셋 포함 + 이름 지정

pyinstaller --onefile --windowed --add-data "assets;assets" --name=MyGame main.py



## AI 활용 내역


Q. 이미지 , 사운드 코드 수정 후 resource\_path() 코드가 적용되지 않은 부분 ai에게 확인 요청

AI : resource\_path() 코드가 적용되지 않은 부분의 해당 코드 위치 제공



Q. 이미지 ,사운드 코드 수정 후 thonny 실행이 안되는 원인 질문

AI : 무한루프, 강제 종료, Thonny 백엔드 충돌 가능성을 설명하고 재실행·백엔드 초기화·재부팅 등의 해결 방법 안내 -> 재실행 후 정상 작동

Q. 이미지 , 사운드 파일을 에셋 폴더에 넣지 않고도 exe 파일에 불러올 수 있는 	방법이 있는지 요청

AI : 
pyinstaller --onefile --windowed ^

--add-data "apple.png;." ^

--add-data "body.png;." ^

--add-data "head.png;." ^

--add-data "back.png;." ^

--add-data "bgm.mp3;." ^

--name=MyGame main.py

-> --add-data 옵션을 사용하여  이미지 파일을 하나씩 개별적으로 exe 파일에 불러오기 가능

