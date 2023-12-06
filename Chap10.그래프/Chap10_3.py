size = 4

class Graph:
    def __init__(self):
        self.adj_mat = [[0 for i in range(size)] for i in range(size)] 
        self.visited = [False] * size 

    def insert_edge(self, start, end):
        self.adj_mat[start][end] = 1
        self.adj_mat[end][start] = 1

    def dfs(self, v):
        self.visited[v] = True
        print("정점 %d ->" % v, end=" ")

        for w in range(size):
            if self.adj_mat[v][w] == 1 and self.visited[w] == False:
                self.dfs(w)

    def main(self):
        edges = [[0,1], [0,2], [0,3], [1,2], [2,3]]
        for start, end in edges:
            self.insert_edge(start, end)
        print("깊이 우선 탐색")
        self.dfs(0)

g = Graph()
g.main()


