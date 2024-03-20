from CPoint import Point
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
if __name__ == "__main__":
    p1 = Point(-4,0)
    p2 = Point(-4,6)
    p3 = Point(-4,8)
    test = GeometryFunctions(p1,p2,p3)
    test.onLine()