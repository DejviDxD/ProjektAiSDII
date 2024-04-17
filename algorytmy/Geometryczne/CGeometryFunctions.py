from CPoint import Point
import numpy as np
class GeometryFunctions:
    def __init__(self,p1 : Point,p2 : Point,p3 : Point) -> None:
        self.p1,self.p2,self.p3 = p1,p2,p3
    def onLine(self):
        check = (p2.x - p1.x)*(p3.y - p1.y) == (p2.y-p1.y)*(p3.x - p1.x)
        if check:
            if (p3.x >= min(p1.x,p2.x) and p3.x <= max(p1.x,p2.x) and p3.y <= max(p1.y,p2.y) and p3.y >= min(p1.y,p2.y)):
                return True
            else:
                return False

    def isHalfLineCutEdge(self):
        if((p2.x <= p1.x and p1.x < p3.x) or (p2.x >= p1.x and p1.y > (p2.y - p3.y)/(p2.x - p3.x) * (p1.x - p2.x) + p2.y)):
            return True
        return False
    # def onPolygon(self):

    def isCuttingSections(self, p4: Point):
        det1 = p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p3.x * p2.y - p1.x * p3.y - p2.x * p1.y
        det2 = p1.x * p2.y + p2.x * p4.y + p4.x * p1.y - p4.x * p2.y - p1.x * p4.y - p2.x * p1.y
        det3 = p3.x * p4.y + p4.x * p1.y + p1.x * p3.y - p1.x * p4.y - p3.x * p1.y - p4.x * p3.y
        det4 = p3.x * p4.y + p4.x * p2.y + p2.x * p3.y - p2.x * p4.y - p3.x * p2.y - p4.x * p3.y
        if(det1 * det2 < 0 and det3 * det4 < 0):
            return True
        if(det1 == 0 and det2 == 0):
            if(min(p1.x,p2.x) <= p3.x and p3.x <= max(p1.x,p2.x)):
                return True
        if det1 == 0:
            if (min(p1.x, p2.x) <= p3.x and p3.x <= max(p1.x, p2.x)):
                    return True
        if det2 == 0:
            if (min(p1.x, p2.x) <= p4.x and p4.x <= max(p1.x, p2.x)):
                    return True
        if det3 == 0:
            if (min(p3.x, p4.x) <= p1.x and p1.x <= max(p3.x, p4.x)):
                    return True
        if det4 == 0:
            if (min(p3.x, p4.x) <= p2.x and p2.x <= max(p3.x, p4.x)):
                    return True
        return False



if __name__ == "__main__":
    p1 = Point(1,1)
    p2 = Point(5,5)
    p3 = Point(3,3)
    p4 = Point(5,2)
    test = GeometryFunctions(p1,p2,p3)
    print(test.isCuttingSections(p4));
