INF = 9999 #무한 상수

class Graph:
    def __init__(self):
        pass
    
    def choose_vertex(self, dist, found): #최소 dist 정점을 찾는 함수
        min = INF
        minpos = -1
        for i in range(len(dist)): # 모든 정점 중에서
            if dist[i]<min and found[i] == False: # 방문하지 않은 최소의 dist 정점
                min = dist[i]
                minpos = i
        return minpos # 최소의 dist 정점을 반환

    def short_path_dijkstra(self, vertex, adj, start):
        vsize = len(vertex) # 정점수
        dist = list(adj[start]) # dist 리스트 생성 및 소기화
        path = [start] * vsize # path 리스트 생성 및 초기화
        found = [False] * vsize # found 리스트 생성 및 초기화
        found[start] = True # 시작정점은 이미 방문 True
        dist[start] = 0 # 시작 정점의 거리 0

        for i in range(vsize): # 정점의 수만큼 반복
            print("step%2d: " % (i+1), dist) # 단계별 dist 리스트 출력
            u = self.choose_vertex(dist, found) # 최소 dist 정점 u 방문
            found[u] = True # u는 방문하여 True

            for w in range(vsize): # 정점의 수만큼 반복
                if not found[w]: # 아직 방문하지 않았다면
                    if dist[u] + adj[u][w] < dist[w]: # 갱신 조건 검사
                        dist[w] = dist[u] + adj[u][w] # dist 리스트 갱신
                        path[w] = u # 이전 정점 갱신
        return path # 탐색한 최단 경로 반환

    def main(self):
        print("Dijkstra Algorithm")
        vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # 노드
        weight = [[0, 7, INF, INF, 3, 10, INF],  # 각 노드에서 가중치
                 [7, 0, 4, 10, 2, 6, INF],
                 [INF, 4, 0, 2, INF, INF, INF],
                 [INF, 10, 2, 0, 11, 9, 4],
                 [3, 2, INF, 11, 0, 13, 5],
                 [10, 6, INF, 9, 13, 0, INF],
                 [INF, INF, INF, 4, 5, INF, 0]]

        start = 0 # 시작정점
        path = self.short_path_dijkstra(vertex, weight, start) # 함수 호출 및 최단 경로 반환받음

        for end in range(len(vertex)): # 최단 경로 출력
            if end != start:
                print("[최단경로: %s -> %s] %s" % (vertex[start], vertex[end], vertex[end]), end=" ")

                while(path[end] != start):
                    print("<- %s" % vertex[path[end]], end=" ")
                    end = path[end]
                print("<- %s" % vertex[path[end]])

g = Graph()
g.main()