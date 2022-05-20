

<div align="center">

  # Wanted Backend Pre Onboarding Project 002 
 

  <img height="200" width="200" src="https://user-images.githubusercontent.com/86823305/167047517-d0abb0fb-654c-4064-87e5-1f9016752fd0.png">

   
  

</div>

## 목차
- [D팀 멤버 소개](#-team-d-member)  
- [개발 기간](#--개발-기간--)  
- [프로젝트 설명 분석](#-프로젝트-설명--분석)
- [프로젝트 개발 조건](#-개발-조건)  
- [프로젝트 요구 조건](#-요구-조건)  
- [ERD](#erd)  
- [구현 기능](#구현-기능)  
- [배포](#-배포)
- [API 명세서](#api-명세서)  
- [Test cases code](#테스트-케이스)  
- [기술 스택](#사용된-기술-스택)  


<div align="center">  

## 👨‍👨‍👦‍👦 Team "D" member  
  
  |권상현|김석재|류성훈|정미정|  
  |:------:|:------:|:------:|:------:|  
  |<img src="https://avatars.githubusercontent.com/u/39396492?v=4" width="200"/> | <img src="https://avatars.githubusercontent.com/u/86823305?v=4" width="200"/> | <img src="https://avatars.githubusercontent.com/u/72593394?v=4" width="200"/> |<img src="https://avatars.githubusercontent.com/u/86827063?v=4" width="200"/> |      
  |[Github](https://github.com/gshduet)|[Github](https://github.com/Cloudblack)|[Github](https://github.com/rsh1994)|[Github](https://github.com/nxxxtyetdecided)|  
  
  <br>


  
|<img height="200" width="380" src="https://retaintechnologies.com/wp-content/uploads/2020/04/Project-Management-Mantenimiento-1.jpg">|<img height="200" width="330" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGElLjafMUhHglmqwh9lRh_sVzOCQyBiPNfQ&usqp=CAU">|
|:------:|:------:|
|💻 [**Team work**](https://mature-citron-a04.notion.site/Wanted_Pre_Onboarding-6af013e2bb3b43739cebc641de4ff558)  | 📒 [**Project page**](https://mature-citron-a04.notion.site/2-b8c6440fee49445ca63ce4d73d8b19e7)|
|공지사항, 컨벤션 공유 등<br> 우리 팀을 위한 룰 |요구사항 분석, 정보 공유 및<br> 원할한 프로젝트를 위해 사용|

  </div> 

  <h2> ⌛ 개발 기간  </h2> 
  2022/05/02  ~ 2022/05/09 

  
# 💻 Project
  ### 💭 프로젝트 설명 & 분석
  - 주어진 데이터를 여러 필터링을 사용하여 레스토랑의 인사이트를 보여주는 API를 만든다

  
<details>
  <summary>누가 사용 할 서비스인가?</summary>
<div markdown="1">

- 크게 세가지 권한 단위로 구분 할 수 있다

  - 서비스 전체를 관리, 프랜차이즈들을 관리하고 정보를 조회 하는 **`API 서비스 관리자`** 
      - 서비스 관리자는 고객은 아니지만 관리를 위해 서비스를 사용하게 될 것이다
  - 해당 프랜차이즈의 음식점과 메뉴(menu)를 관리하고 정보를 조회하는 **`프랜차이즈 관리자`**
      - 지점들의 정보를 분석해 프랜차이즈가 이윤을 추구 하는 전략, 방침을 제시할 수 있다
  - 해당 음식점의 정보를 조회하는 **`음식점 점주`**  
      - 해당 지점의 상권 특성을 분석해 같은 프랜차이즈 내에서도 차별화를 둘 수 있다

</div>
</details>

<details>
  <summary>어떤 관계로 이루어져 있는가?</summary>
<div markdown="1">
         
 [참고: ERD](#erd) 

  -  **`프랜차이즈(Subsidary)`** 는 **`id와 이름으로 구분`** 되며 **`음식 지점`** 들을 가지고있고 그 지점에서 판매하는 **`메뉴`** 를 가지고있다. 나중에는 지점별로 특성에 맞게 변형 될 수 있겠지만 메뉴의 기본 틀은 프랜차이즈를 따라간다  

  - **`음식점(Restaurant)`** 의 **이름(Name)은 프랜차이즈와 주소(Ward) (예시: 버거킹, 서초구 신림동)로** 이루어져있으며 같은 주소에 같은 프랜차이즈가 있을 경우를 대비해 **`호점(Store)`** 이라는 숫자로 구분 할 수 있다
  - **`메뉴(Menu)`** 는 **소속된 프랜차이즈 , 이름 과 가격** 으로 이루어져있다 
  - 음식점에서 나오는 **`결과(Result)`** 는 **한 테이블의 주문 정보** 라고 볼 수 있다 **음식점 , 프랜차이즈 , 결제수단(Payment) , 인원수(number_of_party) , 총금액(total_payment)** 로 이루어져있다.
  - 결과만 봐서는 총 금액은 알 수 있지만 어떤 메뉴를 주문했는지 알 수 가 없어 **결과와 메뉴를 Many to many** 로 연결해주는 **`메뉴결과(ResultMenu)` 는 주문** 이라고 볼 수 있다.   
 - **`메뉴결과(ResultMenu)`** 는 **어떤 메뉴인지 , 어느 테이블(결과) 인지 양(quantity)** 은 얼마나 되는지 표시 할 수 있다.  
 **`할인(discount_rate)` 을 주문에서** 적용 할 수 있게 해 같은 메뉴 몇개 이상시 할인 혹은 직원 할인, 프랜차이즈 프로모션 , 지점에 맞춘 특별 할인등에 유연하게 적용 할 수있다.

</div>
</details>

<details>
  <summary>어떤 정보를 조회(집계) 할 수 있는가?</summary>
<div markdown="1">

- 먼저 필수로 `기간` 과 `시간단위(time_window)` 이 필요하다 그리고 크게 세가지를 기준으로 집계를 할 수 있다.
  - `금액 범위`
  - `결제 수단`
  - `인원 수 `
 
</div>
</details>

   
  ### 🚥 개발 조건 
  
  #### 🙆‍♂️ 필수사항  
    - RDB 사용 - MySQL  
    - Django  
    - REST API V1 구현  
        - POS의 결제 정보를 RDB로 보냅니다  
        - 레스토랑 KPI를 집계  
  #### 🔥 선택사항
    - REST API V2 구현  
    - Unit test codes  
    - REST API Documentation (Swagger UI)  

### 💫 요구 조건

<details>
  <summary>REST API V1</summary>
<div markdown="1">
  
  - 필수  
  
    - 생성  
  
        | 레스토랑 정보 | Restaurant |
        | --- | --- |
        | 주문총계 (총 결제금액, 인원수 등) | Result |
        | 주문결과 (주문 내역) | ResultMenu |
        | 업종 정보 | Subsidary |  
  
        -  POS의 결제 정보를 RDB로 보냅니다
            - 어떤 method를 사용할 것인가?
            - 업로드 해야하는 데이터
                
                → number of a party (인원 수)
                
                → how much they pay (결제 금액)
                
                → restaurant id (레스토랑 id → RDS에서 자동적으로 만들어지는 id)
                
                → timestamp
                
    -  조회
        - 레스토랑별 KPI
            
            관리자는 다양한 필터를 이용해 집계를 확인할 수 있습니다.
            
            -  집계 기능
                - 시간단위
                    
                    → e.g. HOUR, DAY, WEEK, MONTH, YEAR
                    
            -  필터 기능
                - input
                    - 기간 별 (must)
                        
                        → e.g. Start: 2022-04-14 00:01:31 in KT / End: 2022-04-16 00:12:34 in KT
                        
                    - 금액 별 (optional)
                        
                        → e.g., from 20000 won to 100000 won
                        
                    - 인원 별 (optional)
                        
                        → e.g., from 2 to 2
                        
                    - 레스토랑 별 (optional)
                        
                        → e.g., 비비고 (1), 빕스버거 (2)
                        
                - output
                    - 레스토랑 별 매출
                        
                        **집계 예시**
                        
                        DAY time window, 
                        
                        From 2022-02-23 to 2022-02-25 and only for 비비고, 
                        
                        aggregated sales total (price) per restaurant  
                        ![image](https://user-images.githubusercontent.com/86823305/167057808-2e8f0f4d-e749-416b-9c3d-62e767c72cc3.png)

                        
                    - 가장 매출이 높은 시간
                        
                        → (기간 별) 매출 합 정렬
                        
                    - (선택)가장 많이 쓰인 결제수단
                        
                        → (기간 별) 결제수단 합 정렬
                        
                        ![image](https://user-images.githubusercontent.com/86823305/167057841-3dccde78-34ba-400d-8765-79e2ffd0e635.png)
                        
                    - (선택)주로 몇명의 고객이 같이 식사하는지
                        
                        → (기간 별) 그룹 수 평균 정렬
                        
                        ![image](https://user-images.githubusercontent.com/86823305/167057853-d74f8762-ce94-44aa-9823-1ea8c78f20ef.png)
                        
                - 필요한 파라미터
                    - 기간 : start_date , end_date
                    - 금액 : start_price, end_price
                    - 인원 : start_ , end_
                    - 레스토랑별 :
                    - 어떻게 정렬 할 것인지 : 합, 평균, 최대값 등
                
- 선택
    - REST API document - Swagger
    - Test cases code
</div>
</details>


<details>
  <summary>REST API V2</summary>
<div markdown="1">
  
- `생성`
    - 메뉴 생성                   Menu
- `조회`
    - 레스토랑 그룹별 매출액
        
        DAY time window, 
        
        From 2022-02-23 to 2022-02-25 and only for 비비고, 
        
        aggregated sales total (price) per restaurant
        
        ![image](https://user-images.githubusercontent.com/86823305/167057876-8a9d450a-0e17-4db0-bd88-6673bd4953d6.png)
        
    - 레스토랑 지역별 매출액
        
        BR company 상무 Emily는 2022년 3월 한달동안 관악구의 총 매출액을 보고 싶다.
        
    - 레스토랑 메뉴별 매출액
        - e.g : BR company 전무 Amy는 2022년 2월에 빕스버거에서 버거와
        불고기버거의 매출액을 비교하고 싶다.
  
            ![image](https://user-images.githubusercontent.com/86823305/167057887-57fdf75a-3a6b-49a4-9c69-add9cc82a8f5.png)

            
- `(선택) 수정`
    - 가게정보 Restaurant
    - 메뉴         Menu
    - 업종 정보 Subsidary
- `(선택) 삭제`
    - 가게 정보 Restaurant
    - 업종 정보 Subsidary
    - 메뉴         Menu
    - 결과         Result
    - 주문 취소 ResultMenu
- D 팀 추가 option
    - 메뉴 할인
    - 메뉴 토핑 (or 곱빼기)
    - 관리자 테이블 ( 인증 )
        - Restaurant 테이블을 하나의 객체(점주)로 지정해도 무방할 듯.
        - ID, Password, 점주 이름 컬럼만 추가
  </div>
</details>
  
  ## ERD
  
  ![image](https://user-images.githubusercontent.com/86823305/167058689-7a9ccdca-dd6f-462b-b4e3-0e569dce7b27.png)  
  
  
  ## 구현 기능

  - [x] 업종 (Subsidary) CRUD 기능
  - [x] 레스토랑 (Restaurant) CRUD 기능
  - [x] 메뉴 (Menu) CRUD 기능
  - [x] 주문 (Result) Create 기능
  - [x] 조건 별 KPI R(조회)
  - [x] Test cases code - Restaurant, Menu, Subsidary
  - [x] API 명세서 - SWAGGER
  - [ ] 메뉴 할인 
  - [ ] 메뉴 토핑
  - [ ] 관리자 기능
  
  ## 🔥 배포

  docker를 이용해 프로젝트 api를 컨테이너화 하여 EC2에 배포했습니다

  [API Link](http://54.180.147.196/restaurants/)
  
  ## API 명세서
  [API 명세서 (Swagger)](https://app.swaggerhub.com/apis/nxxxtyetdecided8/Bear_Robotics_D/1.0.0#](https://app.swaggerhub.com/apis-docs/nxxxtyetdecided8/Bear_Robotics_D/1.0.0)
  ## 테스트 케이스
  
  ![image](https://user-images.githubusercontent.com/86823305/167321623-2acd83e1-a08f-4b2b-946c-104a3d20b424.png)
  
  Pytest-Django로 구현 된 24개의 테스트 구현, 통과 완료
  
  ## 사용된 기술 스택
  
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.10-3776AB?style=flat&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 4.0.4-092E20?style=flat&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django-DRF 3.13.1-009287?style=flat&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Mysql 8.0.28 -1b9e41?style=flat&logo=Mysql&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker 20.10.14-2496ED?style=flat&logo=docker&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Gunicorn 20.1.0-499848?style=flat&logo=gunicorn&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/NGINX 1.21.6-0ECAD4?style=flat&logo=NGINX&logoColor=white"/>
> 
> - ETC　　　:  <img src="https://img.shields.io/badge/Git-F05032?style=flat-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=flat-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Swagger-FF6C37?style=flat-badge&logo=Swagger&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/AWS EC2-FF9900?style=flat-badge&logo=Amazon AWS&logoColor=white"/>
  
  
  ## 



