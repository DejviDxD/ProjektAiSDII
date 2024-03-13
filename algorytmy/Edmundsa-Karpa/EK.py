
class FF:
    def __init__(self,graf):
        self.graf = graf
        self.ROW = len(graf)

    def bfs(self, s, t, parent):
        visited =[False]*self.ROW
        queue = []
        queue.append(s)
        visited[s] =  True

        while queue:
            u = queue.pop(0)
            for idk , val in enumerate(self.graf[u]):
                if not visited[idk] and val > 0:
                    queue.append(idk)
                    visited[idk] = True
                    parent[idk] = u
                    if idk == t:
                        return True
        return False
    def ford_fukelson(self, source, sink):
        parent = [-1]*self.ROW

        max_capacity = 0
        while(self.bfs(source, sink, parent)):
            path_capacity = float('inf')
            s = sink
            while s != source:
                path_capacity = min(path_capacity, self.graf[parent[s]][s])
                s = parent[s]
            max_capacity += path_capacity

            v = sink
            while v != source:
                u = parent[v]
                self.graf[u][v] -= path_capacity
                self.graf[v][u] += path_capacity
                v = u

        return max_capacity



if __name__ == "__main__":
    vertex,edges = list(map(int,input().split()))
    if edges < vertex - 1:
        print("Nie ma wystarczajaco krawedzi w sieci")
        exit(0)
    graph = [[0 for _ in range (vertex)] for _ in range (vertex)]
    i = 0
    while i < edges:
        x,y,val = list(map(int,input().split()))
        if (x > vertex - 1 or x < 0) or (y > vertex - 1 or y < 0):
            print("Podany wierzcholek jest poza zasiegiem sieci")
            print("Podaj inna krawedz")
        else:
            graph[x][y] = val
            i = i + 1
    source = 0
    sink = vertex-1
    for i in range(vertex):
        print(graph[i])
    g = FF(graph)
    print("Maksymalna przepustowosc w sieci wynosi %d " % g.ford_fukelson(source, sink))







