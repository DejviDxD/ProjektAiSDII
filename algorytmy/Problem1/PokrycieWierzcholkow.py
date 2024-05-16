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
        
if __name__ == "__main__":

    x = Graf()
