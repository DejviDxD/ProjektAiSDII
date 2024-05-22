import math
import sys
sys.path.append("..")

from Geometryczne.CPoint import Point


class Graf:
    def __init__(self,hull,factory) -> None:
        self.hull = hull[:-1]
        self.factory = factory
        self.graf = {i:[] for i in hull}
        self.edges = []
        self.C = {}

    def make_graf(self):
        for i in range(len(self.hull)):
            self.graf[self.hull[i]].append(self.hull[i-1])
            self.graf[self.hull[i-1]].append(self.hull[i])
        self.graf[self.factory] = self.hull

    def print_graf(self):
        for i in self.graf:
            print()
            print(i)
            for j in self.graf[i]:
                print(j,end='')
                print(" ",end='')
            print()

    def min_distance_from_factory(self,graf,hull):
        min_distance = math.sqrt(math.pow(graf[self.factory][0].x-self.factory.x,2) + math.pow(graf[self.factory][0].y -self.factory.y,2))
        min_distance_point = graf[self.factory][0]
        for index in range(1,len(graf[self.factory])):
            distance = math.sqrt(math.pow(graf[self.factory][index].x-self.factory.x,2) + math.pow(graf[self.factory][index].y -self.factory.y,2))
            if(distance < min_distance):
                min_distance = distance
                min_distance_point = graf[self.factory][index]
        return min_distance_point,min_distance

    def apical_coverage(self):
        graf = self.graf.copy()
        hull = self.hull.copy()
        self.C[self.factory] = []
        i = 0
        while len(graf)-1 != 0:
            min_distance_point,min_distance = self.min_distance_from_factory(graf,hull)
            self.C[min_distance_point] = []
            self.C[min_distance_point].append(graf[min_distance_point][0])
            self.C[min_distance_point].append(graf[min_distance_point][1])
            self.C[min_distance_point].append(min_distance)

            self.C[self.factory].append(min_distance_point)
            graf.pop(min_distance_point)
            hull.pop(hull.index(min_distance_point))
            graf[self.factory] = hull

            print(self.C[min_distance_point][0])
            first = True
            if self.C[min_distance_point][0] not in self.edges:
                # if first:
                #     first = False
                #     self.edges.append([])
                #     self.edges[i].append(min_distance_point)
                #     self.edges[i].append(self.C[min_distance_point][0])
                #     self.edges[i].append(math.sqrt(math.pow(self.edges[i][1].y - self.edges[i][0].y,2) + math.pow(self.edges[i][1].x - self.edges[i][0].x,2)))
                #     i+=1
                self.edges.append([])
                self.edges[i].append(min_distance_point)
                self.edges[i].append(self.C[min_distance_point][1])
                self.edges[i].append(math.sqrt(math.pow(self.edges[i][1].y - self.edges[i][0].y,2) + math.pow(self.edges[i][1].x - self.edges[i][0].x,2)))
                self.edges[i].append(False)
                self.edges.append([])
                self.edges[i+1].append(min_distance_point)
                self.edges[i+1].append(self.C[min_distance_point][0])
                self.edges[i+1].append(math.sqrt(math.pow(self.edges[i+1][1].y - self.edges[i+1][0].y,2) + math.pow(self.edges[i+1][1].x - self.edges[i+1][0].x,2)))
                self.edges[i+1].append(False)
            i+=2
        for edge in self.edges:
            for edge2 in self.edges:
                if edge[0] == edge2[1] and edge[1] == edge2[0]:
                    self.edges.remove(edge2)
        del self.C[self.factory]
        return self.C
            

if __name__ == "__main__":

    x = Graf()
