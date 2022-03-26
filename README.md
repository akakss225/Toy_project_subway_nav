# Toy_project_subway_nav

## 이번 Toy_Project는 Python + PyQT + Dijkstra Algorithm을 활용한 지하철 네비게이션 프로그램 개발이다.

1. 지도시각화 도구인 folium 라이브러리를 사용할것
2. 지하철 이름과 좌표가 들어있는 csv를 활용하기위해 csv 라이브러리를 사용할것
3. Python 실행프로그램 UI를 PyQT5를 사용할것
4. 입력한 경로의 최단거리를 위해 Greedy Algorithm인 Dijkstra Algorithm을 사용할것


### PyQt5를 활용한 UI 설계

![ㅁㄴㅇㅁㄴㅇ  Untitled](https://user-images.githubusercontent.com/78843098/160106279-2b0eb46e-603a-458b-9312-945272f85d9a.jpg)

<hr>

## 💻UI 에 역 list를 띄워보자

- 우선 개발에 필요한 라이브러리들을 import 해준다.

<img width="1015" alt="스크린샷 2022-03-26 18 13 33" src="https://user-images.githubusercontent.com/78843098/160233004-cdad055b-d3a2-4357-aea3-dd9b511e6ca9.png">


- 이후 이전에 PyQt5 디자이너를 활용해 만든 ui를 불러오고, csv 파일을 불러들인다.

<img width="1015" alt="스크린샷 2022-03-26 18 13 48" src="https://user-images.githubusercontent.com/78843098/160233151-4465a2ee-0e3a-4b2a-b7d7-b950027eb8d1.png">

<p> 다만 이때 uic를 활용해 읽을 때에는 uic.loadUiType('----')[0] << 처럼 0번째 인덱스를 활용해 읽어준다 (안하면 TypeErr뜸!) </p>

- 정상적으로 동작했는지 확인하기 위해 graph와 location을 찍어보자

graph

<img width="1131" alt="스크린샷 2022-03-26 18 14 21" src="https://user-images.githubusercontent.com/78843098/160233218-3501b837-1dfa-480a-b711-f8bfd712fa49.png">

location

<img width="1131" alt="스크린샷 2022-03-26 18 14 42" src="https://user-images.githubusercontent.com/78843098/160233220-7ba2f992-3203-422d-a384-fe7e3a348f60.png">

<hr>

- WindowClass 를 생성해 상속을 받고, 만들어놓은 UI에 리스트를 추가해서 출력해본다.

<img width="1006" alt="스크린샷 2022-03-26 18 45 49" src="https://user-images.githubusercontent.com/78843098/160234261-01fba1d6-7028-4a15-9f83-15cfa9e3b8d2.png">

<img width="1006" alt="스크린샷 2022-03-26 18 51 38" src="https://user-images.githubusercontent.com/78843098/160234254-f75b303d-9158-4c2b-ae7a-8b800dd0193c.png">

### 🔥🔥 성공적

<img width="518" alt="스크린샷 2022-03-26 18 53 13" src="https://user-images.githubusercontent.com/78843098/160234304-b65a5e7a-4260-4aca-a26e-f3fab9128c49.png">


## 본격적으로 알고리즘을 구현해보자