### IOT 세안제품 냉방 관리 기구

라즈베리파이, DC모터, 터치스크린 기반의 iot 기구

### 개요

터치스크린을 기반으로 로션 스킨등의 화장품을 자동으로 배출하고 냉방으로 관리   
화장품들의 잔량 상태, 기구내 온도,습도를 서버에 저장하고 확인 가능  
터치스크린: GUI(tkinter with python)  
사용자의 손동작을 인식해 원하는 화장품 일정량 배출    
중앙에서 라즈베리파이가(cpu) 제어 및 관리   

### 진행 기간
2019-01-01 ~ 2019-06-20

### 시스템 구성도    
![image](https://user-images.githubusercontent.com/44837403/181682203-4755cea7-d3ca-41c8-9207-6120e32bfb4f.png)

### Specification  

- 라즈베리파이 - 터치스크린 GUI

- 라즈베리파이 - Firebase 연동 환경 구성

- 서버를 통해 화장품 잔량, 구매사이트, 기기내 온도 습도 데이터 관리

- 라즈베리파이에서 온도센서, 모션센서, 스텝모터, dc모터, 릴레이모듈 사용

- 라즈베리파이 화장품 배출을 위한 기능 순서도

- 전동 모터를 활용한 화장품 배출 Auto 작동 기능  
자동화 버튼을 클릭하면 지정해둔 화장품 순서에 따라서 자동으로 배출

- 전동 모터를 활용한 화장품 배출 Manual 작동 기능  
원하는 화장품을 선택해서 수동으로 배출
 
- 모션센서 기반의 손동작 인식

- 펠티어 소자(냉방 장치), 온도 인식센서, 라즈베라피이를 활용한 냉방 온도 제어

- App Inverntor를 통한 스마트폰 연동

### View


- 기구 
![image](https://user-images.githubusercontent.com/44837403/181682420-61e5ec17-2447-41f8-abf7-2635beec2656.png)  


- 터치스크린 화면
![image](https://user-images.githubusercontent.com/44837403/181682268-889ba94b-9022-44ba-bf44-3c70d97f160e.png)  
![image](https://user-images.githubusercontent.com/44837403/181682353-b304aa82-f8bd-4531-8d7a-e8a4a683c7db.png)  

