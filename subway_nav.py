# BFS를 사용하여 최소거리 경로를 찾을 수 있다.
# 다익스트라 알고리즘은 최소 cost를 가지는 경로를 찾을 수 있는 알고리즘이다.
# 여기서 cost는 시간일 수 있고, 시간, 신호등, 주변 경관 등을 적절하게 점수화 한 것일 수도 있다.
# 예를들어 시간이 오래걸리거나 신호등이 많거나 차선이 좁으면 상승하는 cost 함수를 만들 수 있다면, 이 cost함수를 최소화 하는 경로를 찾을 수 있다는 의미이다.
# 이를 이용하면 네비게이션 알고리즘에서 최단경로, 최소시간, 최소비용, 최적 경로라는 이름으로 경로를 탐색하고 사용자는 이 중 적절한 경로를 선택하도록 하는 것이 가능하다.
# 다익스트라 알고리즘은 현재 노드를 통해 연결된 노드로 가는 것과 다른 경로를 통해 가는 cost를 비교하여 더 작은 cost가 있을 경우, 업데이트 하는 방법이다.

# 지도 시각화 모듈
from turtle import color
import folium
# 지도에 Marking을 하는 기능
from folium.map import Marker
# csv 파일을 읽는 모듈
import csv
# 프로그램 UI 설계 모듈
from PyQt5.QtWidgets import *
# ui 파일을 불러올 모듈
from PyQt5 import uic
# 입출력
import sys

# HTML파일을 을 읽을 모듈
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


# PyQt5를 활용해 만든 간단한 UI를 불러옴
form_class = uic.loadUiType('Subway.ui')[0]

# 지하철 역 이름 csv파일을 열어줌
# 이때 encoding='UTF-8-sig'로 설정해주어 첫 데이터 앞의 \ufeff를 지워줌 << 텍스트 읽을때 딸려옴
station_name = open('subway.csv', encoding='UTF-8-sig')
graph = list(csv.reader(station_name))

# 지하철 역 좌표 csv파일을 열어줌
station_loc = open('subwayLocation.csv', encoding='UTF-8-sig')
location = list(csv.reader(station_loc))

# 지하철 역 이름 csv는 [현재역, 다른역, 거리] 로 저장되어있음
# 따라서 모든 역의 이름만을 뽑는 메소드를 작성
def nodes(graph):
    node = set()
    for edge in graph:
        node.add(edge[0])
        node.add(edge[1])
    return sorted(node)

# 역의 이름이 전부 들어있는 set



class MapWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)
        with open("map.html", "r") as f:
            html = f.read()
            self.browser.setHtml(html)
        
        self.setWindowTitle("노선 경로")
    


# 불러온 UI class를 생성해주고, 이를 활용하기위한 메소드들을 넣어줌
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        # 부모 클래스의 init을 상속받음
        super().__init__()
        self.setupUi(self)
        global graph
        
        self.node = nodes(graph)
        # 지하철 역 이름을 모두 PyQt 의 stations(지하철 역 List) 영역에 업로드
        for i in self.node:
            # 지하철 역 이름이 담길 list 이름은 stations이라고 만들어줬음.
            self.stations.addItem(i)
        
        self.btn_sel.clicked.connect(self.locationAdd)
        self.btn_del.clicked.connect(self.locationDelete)
        
        self.mapwindow = MapWindow()
        self.btn_run.clicked.connect(self.programRun)
        
        
    # 선택버튼 클릭시 실행될 메소드
    def locationAdd(self):
        print(self.node[:5])
        # 현재 stations에 존재하는 값을 selected에 addItem해주는 코드
        if len(self.arrive) > 0:
            # 도착역이 이미 있다면 출발역과 도착역을 reset하고, 다시 출발역부터 채워준다.
            self.start.takeItem(0)
            self.arrive.takeItem(0)
            self.start.addItem(self.node[self.stations.currentRow()])
        else:
            # 도착역이 비어있다면
            if len(self.start) > 0:
                # 출발역이 지정되었으면 도착역을 지정해준다.
                self.arrive.addItem(self.node[self.stations.currentRow()])
            else:
                # 출발역이 지정되있지않다면, 출발역먼저 지정해준다.
                self.start.addItem(self.node[self.stations.currentRow()])
        
    # 삭제 버튼 클릭시 실행될 메소드
    def locationDelete(self):
        # 삭제시 선택될 역은 두가지임!
        
        # 첫번째로 출발역
        self.removeItemRow1 = self.start.currentRow()
        # 두번째로 도착역
        self.removeItemRow2 = self.arrive.currentRow()
        
        # 따라서 무엇이 선택되었는지 확인하고 제거함.
        if self.removeItemRow1 == 0:
            self.start.takeItem(self.removeItemRow1)
        elif self.removeItemRow2 == 0:
            self.arrive.takeItem(self.removeItemRow2)
        
    # node와 location을 활용해 좌표를 찾아주는 메소드
    # folium을 활용해 맵에 좌표를 찍기위함
    def findLocation(self, node, location):
        point = []
        for n in node:
            for l in location:
                # 이름을 읽어서 확인하는것
                # 이때, 각 역은 line을 문자열에 ()형태로 포함하기 때문에, 역 이름만 추출하기 위해 slicing해줌
                # 다만, 역마다 문자열 길이가 다르기 때문에, 뒤에서부터 읽어줌. >> 문자열이 반전됨
                if n[-4::-1] == l[0][-1::-1]:
                    point.append([float(l[1]), float(l[2])])
                    break
        return point
    
    # findLocation 메소드로 구한 좌표를 folium을 활용해 맵에 나타내는 메소드
    def mapping(self, node):
        
        middle = len(node) // 2
        
        m = folium.Map(
        # location 속성에 좌표를 입력해줌
        location=node[middle],
        # zoom_start는 초기 크기를 설정해주는 속성
        zoom_start=13
        )
        
        # 출발역에 마커 찍기
        folium.Marker(
            location = node[0],
            icon=folium.Icon("blue")
        ).add_to(m)
        
        # 도착역에 마커 찍기
        folium.Marker(
            location = node[-1],
            icon=folium.Icon("red")
        ).add_to(m)
        
        # 각 역간 이동경로 그리기
        folium.PolyLine(
            locations=node
        ).add_to(m)
        
        # 현재 디렉토리에 html형태로 저장하겠다라는것을 의미.
        m.save("map.html")
    
    
    # 실행버튼 클릭시 실행될 메소드
    # 위에서 작성한 findLocation / mapping 메소드를 활용해야함!
    def programRun(self):
        global location
        
        # 다익스트라 알고리즘 객체를 생성!
        dj = Dijkstra(self.node)
        
        # 출발역 정보
        start = self.start.item(0).text()
        # 도착역 정보
        end = self.arrive.item(0).text()
        
        # 다익스트라 알고리즘의 최단경로를 구하는 getPath를 이용해 node를 만들고
        # 이에대한 좌표를 구해주는 findLocation 메소드를 사용
        # 결과적으로 path 에 좌표가 입력됨.
        path = self.findLocation(dj.getPath(start, end), location)
        self.mapping(path)
        self.mapwindow = MapWindow()
        self.mapwindow.show()
        

class Dijkstra:
    def __init__(self, node):
        # 생성자를 만들때, 그래프를 입력받고, 그래프의 각 노드를 딕셔너리 형태로 만듬.
        # 역
        self.g = {}
        # 최단거리를 구하기 위한 딕셔너리
        self.dist = {}
        for n in node:
            # 일종의 HashTableMap
            self.g[n] = {}
            # 초기 거리를 무한대로 설정하고, 방문하지 않음을 넣어줌.
            self.dist[n] = [float('inf'), "none"]
        
        global graph
        for i in graph:
            self.setEdge(i[0], i[1], int(i[2]))
    
    def setEdge(self, start, end, distance):
        self.g[start][end] = distance
        self.g[end][start] = distance
    
    def getPath(self, start, end):
        
        visit = nodes(graph)
        
        # 특정 키만 포함되도록 필터링 하는 라인함수
        # dictfilt(dist, nodes) >> 
        dictfilt = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
        
        # 시작점을 curNode로 받아서 계속해서 변형시켜줄 예정
        curNode = start
        
        # 현재 노드의 거리는 0으로
        self.dist[curNode][0] = 0
        # start to end 최단거리 구하는 Dijkstra Algorithm 몸체 시작
        while True:
            # 재방문을 방지하기 위해 nodes에서 제거시켜줌 >> 방문처리
            visit.remove(curNode)
            # curNode와 인접한 역 이름 가져오기
            next_to = self.g[curNode]
            
            # 인접한 역을 돌면서
            for i in next_to:
                # 만약 min(다음역의 거리, 현재역 + 다음역 거리) 가 현재까지 책정되있던 다음역까지의 시간보다 작다면
                if min(self.dist[i][0], self.dist[curNode][0] + self.g[curNode][i]) < self.dist[i][0]:
                    # 작은값으로 재설정 해주고
                    self.dist[i][0] = min(self.dist[i][0], self.dist[curNode][0] + self.g[curNode][i])
                    # 어디서부터 왔는지 체크해준다 >> 예를들면 {강남 (2) : [1, 역삼 (2)]} >> 강남은 역삼역에서 1 분이면 온다
                    self.dist[i][1] = curNode
            
            # 그리디 알고리즘을 통해 모든 노드를 돌아보고 각 node간 관계를 설정하기 위해
            # node의 정보가 들어있는 nodes 가 남아있다면, 빌때까지 반복해야함.
            if len(visit) > 0:
                curNode = min(dictfilt(self.dist, visit), key=dictfilt(self.dist, visit).get)
            else:
                break
        
        # Dijkstra Algorithm의 결과를 담을 list생성
        # 역순으로 담으면 편하기 때문에.. 역순으로...
        path = [end]
        # 총 소요시간을 계산할 list
        dist = []
        
        # Dijkstra Algorithm을 통해 리뉴얼된 self.dist를 통해 시작과 끝의 경로를 구해줌
        # 조건은 start == end 가 될때까지로.
        while end != start:
            path.append(self.dist[end][1])
            dist.append(self.dist[end][0])
            end = self.dist[end][1]
            
        # 역순으로 넣었기 때문에, 역순으로 호출해주면, 최단시간 경로를 구해준다.
        return path[::-1]
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    # myWindow = MapWindow()
    myWindow.show()
    app.exec_()
    
station_name.close()
station_loc.close()