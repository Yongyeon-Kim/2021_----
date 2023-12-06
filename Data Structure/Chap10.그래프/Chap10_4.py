size = 4

class Graph:
    class Node:
        def __init__(self, v):
            self.vertex = v
            self.link = None

    def __init__(self):
        self.adj_mat = [None for _ in range(size)]
        self.visited = [False for _ in range(size)]

    def insert_edge(self, u, v):
        self.node = self.Node(v)
        self.node.link = self.adj_mat[u]
        self.adj_mat[u] = self.node

    def dfs(self, v):
        self.visited[v] = True
        print("정점 %d -> " % v, end=" ")
        w = self.adj_mat[v]

        while w!=None:
            if w.link != None:
                w = w.link
            else:
                self.dfs(w.vertex)
                break


    def main(self):
        edges = [[0,1], [0,2], [0,3], [1,2], [2,3]]
        for u, v in edges:
            self.insert_edge(u, v)
        self.dfs(0)
        
g = Graph()
g.main()


