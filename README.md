# Toy_project_subway_nav

## 이번 Toy_Project는 Python + PyQT + Dijkstra Algorithm을 활용한 지하철 네비게이션 프로그램 개발이다.

1. 지도시각화 도구인 folium 라이브러리를 사용할것
2. 지하철 이름과 좌표가 들어있는 csv를 활용하기위해 csv 라이브러리를 사용할것
3. Python 실행프로그램 UI를 PyQT5를 사용할것
4. 입력한 경로의 최단거리를 위해 Greedy Algorithm인 Dijkstra Algorithm을 사용할것


### PyQt5를 활용한 UI 설계

![ㅁㄴㅇㅁㄴㅇ  Untitled](https://user-images.githubusercontent.com/78843098/160106279-2b0eb46e-603a-458b-9312-945272f85d9a.jpg)

<hr>

# 💻UI 에 역 list를 띄워보자

- 우선 개발에 필요한 라이브러리들을 import 해준다.

<img width="1015" alt="스크린샷 2022-03-26 18 13 33" src="https://user-images.githubusercontent.com/78843098/160233004-cdad055b-d3a2-4357-aea3-dd9b511e6ca9.png">


- 이후 이전에 PyQt5 디자이너를 활용해 만든 ui를 불러오고, csv 파일을 불러들인다.

<img width="1015" alt="스크린샷 2022-03-26 18 13 48" src="https://user-images.githubusercontent.com/78843098/160233151-4465a2ee-0e3a-4b2a-b7d7-b950027eb8d1.png">

<b><i>다만 이때 uic를 활용해 읽을 때에는 uic.loadUiType('----')[0] << 처럼 0번째 인덱스를 활용해 읽어준다 (안하면 TypeErr뜸!)</i></b>

- 정상적으로 동작했는지 확인하기 위해 graph와 location을 찍어보자

graph

<img width="1131" alt="스크린샷 2022-03-26 18 14 21" src="https://user-images.githubusercontent.com/78843098/160233218-3501b837-1dfa-480a-b711-f8bfd712fa49.png">

location

<img width="1131" alt="스크린샷 2022-03-26 18 14 42" src="https://user-images.githubusercontent.com/78843098/160233220-7ba2f992-3203-422d-a384-fe7e3a348f60.png">

<hr>

- WindowClass 를 생성해 상속을 받고, 만들어놓은 UI에 리스트를 추가해서 출력해본다.

<img width="1000" alt="스크린샷 2022-03-26 20 08 51" src="https://user-images.githubusercontent.com/78843098/160236745-8dccb965-59df-4d76-9f3b-deea0c4d5879.png">

<img width="1006" alt="스크린샷 2022-03-26 18 51 38" src="https://user-images.githubusercontent.com/78843098/160234254-f75b303d-9158-4c2b-ae7a-8b800dd0193c.png">

### 🔥🔥 성공적

<img width="519" alt="스크린샷 2022-03-26 20 09 07" src="https://user-images.githubusercontent.com/78843098/160236742-aa0728b5-c36f-42f5-9d6d-b6d3e14df7dc.png">



# 💻본격적으로 알고리즘을 구현해보자

- Dijkstra Algorithm의 뼈대를 만든다. 객체를 적극 활용! 추가적으로 출력까지 해본다.

<img width="1007" alt="스크린샷 2022-03-26 19 15 49" src="https://user-images.githubusercontent.com/78843098/160235042-0ecb0058-d9d2-4615-822d-0eb0bf71c55d.png">

- 출력 결과(우웩)

<img width="1132" alt="스크린샷 2022-03-26 19 17 40" src="https://user-images.githubusercontent.com/78843098/160235104-d86c5773-4629-41de-8ab4-97c04afef190.png">


- 알고리즘에 가지고있는 데이터를 이용해 각 역간 걸리는 시간을 설정해주는 <i>setEdge()</i> 를 생성해준다.

<img width="999" alt="스크린샷 2022-03-26 19 50 20" src="https://user-images.githubusercontent.com/78843098/160236175-660374ab-60cf-4ee9-955e-94fbf9799132.png">

- 출력 결과

<img width="1132" alt="스크린샷 2022-03-26 19 50 42" src="https://user-images.githubusercontent.com/78843098/160236225-ae118520-f3c3-4859-89f6-942078278d78.png">


- 본격적인 Dijkstra Algorithm의 몸체를 구현해보자. <i>getPath()</i> 메소드 구현

<img width="1015" alt="스크린샷 2022-03-27 18 11 57" src="https://user-images.githubusercontent.com/78843098/160274829-45865957-7946-4100-b85f-bf3a511892be.png">
<img width="1015" alt="스크린샷 2022-03-27 18 12 12" src="https://user-images.githubusercontent.com/78843098/160274898-4cce3cca-6dca-4cc8-b97c-16e1c92dea28.png">
<img width="1015" alt="스크린샷 2022-03-27 18 12 25" src="https://user-images.githubusercontent.com/78843098/160274905-fc995312-9d40-47c7-9d62-2df2cde71247.png">

- 예시로 강남(2) ~ 강변(2) 의 경로를 구해보자.

<img width="1015" alt="스크린샷 2022-03-27 18 17 52" src="https://user-images.githubusercontent.com/78843098/160274983-83f6a589-71f1-4c82-ac54-0b2c0fe192e5.png">

### 🔥🔥 성공적

<img width="1130" alt="스크린샷 2022-03-27 18 18 06" src="https://user-images.githubusercontent.com/78843098/160275000-fe17b490-52c4-49e5-a7a2-b40920ba8ba4.png">


<hr>

# 💻Dijkstra Algorithm 을 활용해 프로그램을 적용시켜보자!

- 선택 버튼 클릭시, UI의 좌측 역 list의 값이 오른쪽 선택된 역으로 이동해야함!
- 일전에 작성해둔 WindowClass에 <i>locationAdd()</i> 메소드를 구현해준다.

<img width="1021" alt="스크린샷 2022-03-27 19 02 20" src="https://user-images.githubusercontent.com/78843098/160276491-43deb9cb-dfa2-4622-8970-5f3c9b6a5581.png">

### 🔥🔥 성공적...?

<img width="519" alt="스크린샷 2022-03-27 19 02 48" src="https://user-images.githubusercontent.com/78843098/160276461-3cb11184-1d12-4cd6-9922-b6577e2539fe.png">
<img width="519" alt="스크린샷 2022-03-27 19 02 56" src="https://user-images.githubusercontent.com/78843098/160276466-d6e1f2f6-443e-4f08-8ca7-4965d4c0a8ba.png">

- 일줄알았으나...

<img width="519" alt="스크린샷 2022-03-27 19 03 09" src="https://user-images.githubusercontent.com/78843098/160276468-1d5c25a5-01f1-4c05-9692-33bfcef97d4a.png">

여러개가 추가가 된다...

이를 해결하기 위해 UI를 조금 설계해야할듯 합니다...

- 조금 바꾼 UI

<img width="519" alt="스크린샷 2022-03-27 19 12 32" src="https://user-images.githubusercontent.com/78843098/160276729-27bce452-896f-443a-b1d6-ce69f1d7f00a.png">

- 조금 바꾼 <i>locationAdd()</i> 메소드

<img width="1001" alt="스크린샷 2022-03-27 19 29 54" src="https://user-images.githubusercontent.com/78843098/160277312-a92d9fd8-90e8-4db9-a288-b6848658c0a5.png">

- 두근두근....

<img width="518" alt="스크린샷 2022-03-27 19 31 36" src="https://user-images.githubusercontent.com/78843098/160277347-37f858c9-6715-4e03-a255-1b77dd0587b4.png">

### 🔥🔥 성공적!!

<img width="518" alt="스크린샷 2022-03-27 19 31 41" src="https://user-images.githubusercontent.com/78843098/160277351-63921dca-93e5-4b4c-b5d7-143fc22bbc60.png">


- 그럼 다음으로 Delete 기능을 구현해야한다. 따라서 <i>locationDelete()</i> 메소드를 구현해준다.

<img width="991" alt="스크린샷 2022-03-28 19 32 18" src="https://user-images.githubusercontent.com/78843098/160379998-c5284d2c-56f0-4413-b301-a0a69b838986.png">

- 🛠 참고로 WindowClass 생성자인 __init__ 에 아래와 같이 click이벤트를 연결해줘야 됨!

<img width="999" alt="스크린샷 2022-03-28 19 19 43" src="https://user-images.githubusercontent.com/78843098/160378802-bf10ebf4-8fac-4b31-a41d-756e5533bf68.png">

- 결과는..?

<img width="516" alt="스크린샷 2022-03-28 19 21 24" src="https://user-images.githubusercontent.com/78843098/160378868-dd48d10e-4dab-4474-b22c-64c06d6708bc.png">

### 🔥🔥 성공적

<img width="516" alt="스크린샷 2022-03-28 19 21 29" src="https://user-images.githubusercontent.com/78843098/160378941-bf1b2986-af74-4d4d-9022-e091d7487b10.png">
<img width="516" alt="스크린샷 2022-03-28 19 21 37" src="https://user-images.githubusercontent.com/78843098/160378950-859fc3d4-eee2-405a-b811-98ada8486200.png">

- 이제 실제로 프로그램을 실행시키기 위한 메소드를 작성해야한다!

기본적으로 Dijkstra Algorithm을 활용해 경로상의 역 명을 list형태로 받아봤다.

따라서 역 명을 기준으로 location list를 활용해 각 역의 좌표를 구하는 코드가 필요하다.

- <i>findLocation()</i>은 UI에서 입력받은 역 간 최단거리를 나타내는 list를 통해 좌표를 구해주는 메소드다.

<img width="991" alt="스크린샷 2022-03-28 19 50 11" src="https://user-images.githubusercontent.com/78843098/160382821-b7c01710-2c38-46ea-a8ae-e4b10da129be.png">


- 이후, findLocation 메소드의 결과로 folium을 사용해줄 <i>mapping()</i> 메소드를 구현해준다.

<img width="991" alt="스크린샷 2022-03-30 14 24 07" src="https://user-images.githubusercontent.com/78843098/160757235-5a95a9ea-8bf6-4277-81b8-835358247922.png">

- 네비게이션의 꽃인 경로를 찾아주고, 맵에 띄워주는 '실행' 버튼 구현!

<img width="991" alt="스크린샷 2022-03-30 14 35 26" src="https://user-images.githubusercontent.com/78843098/160758543-3cd7ddf3-736c-4a26-8c11-8c16d60d2f87.png">

<img width="991" alt="스크린샷 2022-03-30 14 35 36" src="https://user-images.githubusercontent.com/78843098/160758550-9de02325-5e64-4e63-9fcd-61e88ca7afb0.png">

- 두근두근 실행!

<img width="518" alt="스크린샷 2022-03-30 14 37 52" src="https://user-images.githubusercontent.com/78843098/160758824-1e16abbf-daf0-4f25-bb95-7b82708e9bf2.png">

<img width="202" alt="스크린샷 2022-03-30 14 38 03" src="https://user-images.githubusercontent.com/78843098/160758859-57ed8d52-4631-4af5-b119-7bf63748c30f.png">

- 짜자잔~

<img width="1440" alt="스크린샷 2022-03-30 14 38 52" src="https://user-images.githubusercontent.com/78843098/160759043-6994e114-defe-4d1f-b985-07c2d7119fdf.png">

우선, 시작역의 위치만을 찍은것이기 때문에, 경복궁역의 위치가 출력되는것을 볼 수 있다!

이제 완벽한 네비게이션의 기능을 보여주고자 출발역과 도착역에 Marker를 달아보자.

- <i>mapping()</i> 메소드 리펙토링

<img width="1005" alt="스크린샷 2022-03-30 14 44 31" src="https://user-images.githubusercontent.com/78843098/160759754-dbe6edf8-2474-4c03-a5aa-ee85ef8a64fd.png">

- 실행결과

<img width="1005" alt="스크린샷 2022-03-30 14 45 54" src="https://user-images.githubusercontent.com/78843098/160759914-6474cbd4-87d5-407c-9fb8-54328012d7f1.png">

출발역은 빨간색, 도착역은 파란색 마커가 찍힌것을 볼 수 있다!

- 마지막으로, 각 역간 이동경로를 연결시켜줘야한다!

<img width="1005" alt="스크린샷 2022-03-30 14 55 14" src="https://user-images.githubusercontent.com/78843098/160761171-60c4788a-0e68-4369-acf7-2a6bea1a5511.png">

- 실행결과

<img width="1005" alt="스크린샷 2022-03-30 14 55 24" src="https://user-images.githubusercontent.com/78843098/160761158-0a3a35e3-9b1f-4929-b006-3905644d3924.png">

마지막으로, 처음 맵이 보여주는 위치를 역의 중간으로 잡아주는 코드를 짠다!

