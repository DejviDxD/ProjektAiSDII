import math
import sys
sys.path.append("..")

from Geometryczne.CPoint import Point


class Graf:
    def __init__(self,hull,factory) -> None:
        self.hull = hull[:-1]
        self.factory = factory
        self.graf = {i:[] for i in hull}

    def make_graf(self):
        for i in range(len(self.hull)):
            self.graf[self.hull[i]].append(self.hull[i-1])
            self.graf[self.hull[i-1]].append(self.hull[i])
        self.graf[self.factory] = self.hull
    def print_graf(self):
        for i in self.graf:
            print()
            print(i.x,i.y)
            for j in self.graf[i]:
                print(j.x,j.y,end='')
                print(" ",end='')
            print()

    def min_distance_from_factory(self):
        min_distance = math.sqrt(math.pow(self.graf[self.factory][0].x-self.factory.x,2) + math.pow(self.graf[self.factory][0].y -self.factory.y,2))
        for index in range(1,len(self.graf[self.factory])):
            distance = math.sqrt(math.pow(self.graf[self.factory][index].x-self.factory.x,2) + math.pow(self.graf[self.factory][index].y -self.factory.y,2))
            if(distance < min_distance):
                min_distance = distance
        return min_distance

if __name__ == "__main__":

    x = Graf()
