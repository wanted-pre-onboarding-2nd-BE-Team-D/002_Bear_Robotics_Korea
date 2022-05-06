

<div align="center">

  # Wanted Backend Pre Onboarding Project 002 
 

  <img height="200" width="200" src="https://user-images.githubusercontent.com/86823305/167047517-d0abb0fb-654c-4064-87e5-1f9016752fd0.png">

   
  

</div>

## 목차

<div align="center">  
  <h2> 👨‍👨‍👦‍👦 Team "D" member  </h2>
  
  |권상현|김석재|류성훈|정미정|  
  |:------:|:------:|:------:|:------:|  
  |<img src="https://avatars.githubusercontent.com/u/39396492?v=4" width="200"/> | <img src="https://avatars.githubusercontent.com/u/86823305?v=4" width="200"/> | <img src="https://avatars.githubusercontent.com/u/72593394?v=4" width="200"/> |<img src="https://avatars.githubusercontent.com/u/86827063?v=4" width="200"/> |      
  |[Github](https://github.com/gshduet)|[Github](https://github.com/Cloudblack)|[Github](https://github.com/rsh1994)|[Github](https://github.com/nxxxtyetdecided)|  
  |뭘 넣을지 미정|ㅇㅇ|ㅇㅇ|ㅇㅇ|  
  <br>
  
  </div> 
  <h2> 💻 개발 기간  </h2> 
  2022/05/02  ~ 2022/05/06 
  <h2> 💻 어떻게 일했나?  </h2>  
   
  💻 [Team page](https://mature-citron-a04.notion.site/Wanted_Pre_Onboarding-6af013e2bb3b43739cebc641de4ff558)    
  📒 [Project page](https://mature-citron-a04.notion.site/2-b8c6440fee49445ca63ce4d73d8b19e7)
  
## 💻 Project
  ### 💻 프로젝트 설명 
  주어진 데이터를 여러 필터링을 사용하여 레스토랑의 인사이트를 보여주는 API를 만든다
  ### 💻 개발 조건 
  
  #### 필수사항  
    - RDB 사용 - MySQL  
    - Django  
    - REST API V1 구현  
        - POS의 결제 정보를 RDB로 보냅니다  
        - 레스토랑 KPI를 집계  
  #### 선택사항
    - REST API V2 구현  
    - Unit test codes  
    - REST API Documentation (Swagger UI)  

### 요구 조건

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
  
        - POS의 결제 정보를 RDB로 보냅니다
            - 어떤 method를 사용할 것인가?
            - 업로드 해야하는 데이터
                
                → number of a party (인원 수)
                
                → how much they pay (결제 금액)
                
                → restaurant id (레스토랑 id → RDS에서 자동적으로 만들어지는 id)
                
                → timestamp
                
    - `조회`
        - 레스토랑별 KPI
            
            관리자는 다양한 필터를 이용해 집계를 확인할 수 있습니다.
            
            - 집계 기능
                - 시간단위
                    
                    → e.g. HOUR, DAY, WEEK, MONTH, YEAR
                    
            - 필터 기능
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
  
  ## 모델링
  
  ![image](https://user-images.githubusercontent.com/86823305/167058689-7a9ccdca-dd6f-462b-b4e3-0e569dce7b27.png)
  
  ## 구현 기능
  
  ## API 명세서
  
  ## 테스트 케이스
  
  ## 사용된 기술 스택
  
  > - Back-End :  <img src="https://img.shields.io/badge/Python 3.10-3776AB?style=flat&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 4.0.4-092E20?style=flat&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/mysql 5.0-1b9e41?style=flat&logo=Mysql&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django_rest_freamwork 3.13.1-009287?style=flat&logo=Django-rest-freamwork&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Pytest 7.1.2-0A9EDC?style=flat&logo=Pytest&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=flat-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=flat-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Swagger-FF6C37?style=flat-badge&logo=Swagger&logoColor=white"/>
  
 

  
  
  
  ## 


<div align="center"> 
  
  ![image](http://image.pullbbang.com/pull2012/upload/board/2018/2/20180217010016472.gif)
<h3>End</h3>
  </div> 
