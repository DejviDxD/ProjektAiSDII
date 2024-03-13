
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
        maks_przepustowosc = 0
        while(self.bfs(source, sink, parent)):
            sciezka_przepustowosci = float('inf')
            s = sink
            while s != source:
                sciezka_przepustowosci = min(sciezka_przepustowosci, self.graf[parent[s]][s])
                s = parent[s]
            maks_przepustowosc += sciezka_przepustowosci

            v = sink
            while v != source:
                u = parent[v]
                self.graf[u][v] -= sciezka_przepustowosci
                self.graf[v][u] += sciezka_przepustowosci
                v = u

        return maks_przepustowosc




vertex,edges = list(map(int,input().split()))
graph = [[0 for _ in range (vertex)] for _ in range (vertex)]

for i in range (edges):
    x,y,val = list(map(int,input().split()))
    graph[x][y] = val
source = 0
sink = vertex-1
for i in range(vertex):
    print(graph[i])
g = FF(graph)
print("The maximum possible flow is %d " % g.ford_fukelson(source, sink))







