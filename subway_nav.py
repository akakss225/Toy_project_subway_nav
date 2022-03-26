# BFS를 사용하여 최소거리 경로를 찾을 수 있다.
# 다익스트라 알고리즘은 최소 cost를 가지는 경로를 찾을 수 있는 알고리즘이다.
# 여기서 cost는 시간일 수 있고, 시간, 신호등, 주변 경관 등을 적절하게 점수화 한 것일 수도 있다.
# 예를들어 시간이 오래걸리거나 신호등이 많거나 차선이 좁으면 상승하는 cost 함수를 만들 수 있다면, 이 cost함수를 최소화 하는 경로를 찾을 수 있다는 의미이다.
# 이를 이용하면 네비게이션 알고리즘에서 최단경로, 최소시간, 최소비용, 최적 경로라는 이름으로 경로를 탐색하고 사용자는 이 중 적절한 경로를 선택하도록 하는 것이 가능하다.
# 다익스트라 알고리즘은 현재 노드를 통해 연결된 노드로 가는 것과 다른 경로를 통해 가는 cost를 비교하여 더 작은 cost가 있을 경우, 업데이트 하는 방법이다.

# 지도 시각화 모듈
import folium
# 지도에 Marking을 하는 기능
from folium.map import Marker
# csv 파일을 읽는 모듈
import csv
# 프로그램 UI 설계 모듈
from PyQt5.QtWidgets import *
# ui 파일을 불러올 모듈
from PyQt5 import uic

import sys


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
node = nodes(graph)


# 불러온 UI class를 생성해주고, 이를 활용하기위한 메소드들을 넣어줌
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        # 부모 클래스의 init을 상속받음
        super().__init__()
        self.setupUi(self)
        
        global node
        # 지하철 역 이름을 모두 PyQt 의 stations(지하철 역 List) 영역에 업로드
        for i in node:
            # 지하철 역 이름이 담길 list 이름은 stations이라고 만들어줬음.
            self.stations.addItem(i)
        
        
    # 선택버튼 클릭시 실행될 메소드
    def locationAdd(self):
        global graph
        
        # 현재 stations에 존재하는 값을 selected에 addItem해주는 코드
        if len(self.selected) == 2:
            self.selected.take
        self.selected.addItem(graph[self.stations.currentRow()][0])
    
    # 삭제 버튼 클릭시 실행될 메소드
    def locationDelete(self):
        self.removeItemRow = self.selected.currentRow()
        self.selected.takeItem(self.removeItemRow)
    
    # 노드와 좌표를 활용해 위치를 찾아주는 메소드
    def findLocation(self):
        global node
        global location
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
    
    
    # 실행버튼 클릭시 실행될 메소드
    def programRun(self):
        start = self.selected.item(0).text()
        end = self.selected.item(1).text()
        
        

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
        dictfilt = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
        return dictfilt

# dj = Dijkstra(node)
# print(dj.g)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
station_name.close()
station_loc.close()